from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from comWindows import Ui_comWIndows
from mainWindows import Ui_MainWindow


from serial import Serial

import serial.tools.list_ports
import bluetooth
import sys
import os
import time
import easygui

class Main(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.setup_connections()
        self.show()
        self.interface_2.appendPlainText("> Welcome on GCodeSender app !!!")
        self.writting = False
        self.s = None

    def connect(self):
        if(self.writting):
             self.interface_2.appendPlainText("> Sending in progress, cannot create new connection")
             return False

        self.interface_2.appendPlainText("> Bluetooth and COM ports searching can take a while, please be patient ... ")
        bluetooth_name = self.enter_bluetooth_name()
        if(bluetooth_name!=None):
            if(self.verify_bluetooth_conf(bluetooth_name)):
                self.speed = self.get_speed()
                self.get_com_port()
                      
    
    def enter_bluetooth_name(self):
        text, okPressed = QtWidgets.QInputDialog.getText(self, "Bluetooth conf","Bluetooth name:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            return text

    def get_speed(self):
        check_speed = False
        while(check_speed==False):
                d, okPressed =QtWidgets.QInputDialog.getInt(self, "Baud rate","Value:",min=9600,max=115200)
                if okPressed:
                    if(d in [ 9600, 14400, 19200, 28800, 38400, 57600, 115200]):
                        check_speed=True
                    else:
                        self.interface_2.appendPlainText("> Speed incorrect, must be : 9600, 14400, 19200, 28800, 38400, 57600 or  115200")
        return d


    def setup_connections(self):
        self.startButton.clicked.connect(self.connect)
        self.gCodeButton.clicked.connect(self.send)
        self.stopButton.clicked.connect(self.stop)
        self.originButton.clicked.connect(self.origin)

    def origin(self):
        if(self.is_connected()==False ):
            self.interface_2.appendPlainText("> Please connect first")
            return False
        if(self.writting):
            self.interface_2.appendPlainText("> Please wait until the current file be sent ")
        else:
            self.s.write(("G1AX0.0AY0.0" + '\n').encode()) # Send g-code block
            self.interface_2.appendPlainText('> Sending: ' + "G1AX0.0AY0.0")


    def stop(self):
        try:
            if(self.s.isOpen()):
                self.s.close()
        except:
            pass
        self.interface_2.appendPlainText("> Disconnected")


    def is_connected(self):
        try:
            if(self.s.isOpen()):
                return True
            return False

        except:
            return False



    def send(self):
        if(self.is_connected()==False ):
             self.interface_2.appendPlainText("> Please connect first")
             return False
        if(self.writting ):
             self.interface_2.appendPlainText("> Stopping current writting")
             self.sender.quit()

        filename = easygui.fileopenbox()
        try:
            f = open(filename,"r")
            number_of_lines=0
            for line in f:
	            number_of_lines+=1
            f.close()
            f = open(filename,"r")
            self.output.clear()
            if(self.s.isOpen()):
                self.sender = Send(self.s,self.output,self.interface_2,f,self.progressBar,number_of_lines)
                self.writting = True
                self.sender.start()
                self.sender.signal.connect(self.finished)
        except Exception as inst:
            self.interface_2.appendPlainText("> Detected troubles in file or connection. Stop sending.")

    def finished(self,sent):
        self.writting = False
        if(sent):
            self.interface_2.appendPlainText("> File sent")
        else:
            self.interface_2.appendPlainText("> An error occured, please retablish connection and check file")
            self.connected = False
        



    def open_port(self):

        port = self.comWidget.listWidget.selectedItems()[0].text()
        if(self.speed!=None):
            try:
                self.s = Serial(port,self.speed)
                self.interface_2.appendPlainText("> Connection on %s etablished"%port)
                self.comWindow.hide()

            except Exception as e:
                self.interface_2.appendPlainText("> Port cannot be openned. Check COM port value in the new window")
                os.system("control printers")
               
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('baud rate unknow')
       




    def get_com_port(self):
        self.interface_2.appendPlainText("> Searching COM ports....")
        self.comWindow = QtWidgets.QMainWindow()
        self.comWidget = Ui_comWIndows()
        self.comWidget.setupUi(self.comWindow)
        comPorts=list(serial.tools.list_ports.comports())
        for COM,des,hwenu in comPorts :
            self.comWidget.listWidget.addItem("%s"%(COM))
        self.comWindow.show()
        self.comWidget.pushButton.clicked.connect(self.open_port)




    def verify_bluetooth_conf(self,device_name):
        if(device_name=="none"):
            self.interface_2.appendPlainText("> Disabling Bluetooth. ")
            return True

        self.interface_2.appendPlainText("> Searching devices....")
        nb=bluetooth.discover_devices(duration=2,lookup_names=True)
        check = False
        for addr,name in list(nb):
            if(device_name == name ):
                check = True
                break
        if(check==True):
               self.interface_2.appendPlainText("> Device found!!  already paired: %s %s"%(addr,name))
               return True
        else:
            self.interface_2.appendPlainText("> Your devices is not paired.")
            self.interface_2.appendPlainText("> Lauch stopped")
            self.interface_2.appendPlainText("> Please paired the %s device first "%(device_name))
            time.sleep(1)
            os.system("start ms-settings:bluetooth")
            return False



class Send(QThread):

    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self,s,output,interface_2, f,progressBar,lineN):
        QThread.__init__(self)
        self.interface_2= interface_2
        self.output = output
        self.s = s
        self.f = f
        self.progressBar = progressBar
        self.progressBar.setValue(0)
        self.lineN = lineN

    def removeComment(self,string):
        if (string.find(';')==-1 or string.find('(') > 0):
            return string
        else:
            return string[:string.index(';')]


    # run method gets called when we start the thread
    def run(self):
        try:
            self.interface_2.appendPlainText("> Sending gcode")
            counter=0
            v=0
            for line in self.f:
                temp = int((counter/self.lineN)*100)
                if(temp>v):
                    self.progressBar.setValue(temp)
                    v=temp

                l = self.removeComment(line)
                l = l.replace(" ","A")
                # Strip all EOL characters for streaming
                l = l.strip() 
                if  (l.isspace()==False and len(l)>0) :
                    l+='A'
                    self.interface_2.appendPlainText('> Sending: ' + l)
                    self.s.write((l + '\n').encode()) # Send g-code block
                    time.sleep(0.3)
                    grbl_out = self.s.readline() # Wait for response with carriage return
                    while grbl_out!=b'OK\r\n':
                        self.output.appendPlainText(str(grbl_out.strip() ))
                        grbl_out = self.s.readline() # Wait for response with carriage return
                        time.sleep(0.05)
                    grbl_out = ""
                    counter+=1
        except Exception as inst:
            self.progressBar.setValue(100)
            self.signal.emit(False)

        self.progressBar.setValue(100)
        self.signal.emit(True)


        



app = QtWidgets.QApplication([])
nc = Main()
app.exec_()
