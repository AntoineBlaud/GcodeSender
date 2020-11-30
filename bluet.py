import serial.tools.list_ports
import bluetooth
import sys
import os
import time
import easygui

PAUSE_INTERVAL = 600

def verify_bluetooth_conf(device_name):
    nb=bluetooth.discover_devices(duration=5,lookup_names=True)
    check = False
    for addr,name in list(nb):
        if(device_name == name ):
            check = True
            break
    if(check==True):
        print("Device found!!  already paired: %s %s"%(addr,name))
    else:
        print("Your devices is not paired.")
        print("Please %s paired the device"%(device_name))
        time.sleep(0.8)
        os.system("start ms-settings:bluetooth")


def list_com_port():
    comPorts=list(serial.tools.list_ports.comports())
    for COM,des,hwenu in comPorts :
            print("%s"%(COM))

def select_file():
    file = easygui.fileopenbox()
    return file

def open_printer_control():
    os.system("control printers")


def connect(COM,speed):
    s = serial.Serial(COM,speed)
    print('Opening Serial Port')
    return s



def checkTime(s, time1):
	# Get the current time 
	time2 = time.clock()
	#If 600 secondes have elapsed, we're taking a pause
	if ((time2-time1) > PAUSE_INTERVAL):	
		s.write("E0A".encode()) #E0A is the instruction to stop  drivers
		print("Pause de 30 sec afin d'éviter le surchauffement des drivers ...")
		time.sleep(30)
		print("Fin de la pause !")
		s.write("E1A".encode()) #E1A is the instruction to relauch drivers
		return time.clock()
	# Else we keep time1 value
	else:
		return time1


def process_sendind(s,f):
    print ('Sending gcode\n\n')
    # Start the Chrono
    time1 = time.clock()
    for line in f:
        l = removeComment(line)
        l = l.replace(" ","A")
        # Strip all EOL characters for streaming
        l = l.strip() 
        #Check execution time > PAUSE_INTERVAL and stop 2 min if it is the case
        time1 = checkTime(s,time1)
        if  (l.isspace()==False and len(l)>0) :
            l+='A'
            print ('Sending: ' + l)
            s.write((l + '\n').encode()) # Send g-code block
            time.sleep(0.3)
            print("Waiting responses :\n")
            grbl_out = s.readline() # Wait for response with carriage return
            while grbl_out!=b'OK\r\n':
                print(grbl_out)
                grbl_out = s.readline() # Wait for response with carriage return
                time.sleep(0.05)
            print(grbl_out+"\n")
            grbl_out = ""


def count_line(f):
    number_of_lines = 0
    for line in f:
	    number_of_lines+=1
    return number_of_lines


#verify_bluetooth_conf("printer")