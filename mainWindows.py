# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\antoi\Documents\GitHub\Arduino\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 691)
        MainWindow.setMinimumSize(QtCore.QSize(808, 691))
        MainWindow.setMaximumSize(QtCore.QSize(808, 691))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gCodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.gCodeButton.setGeometry(QtCore.QRect(680, 40, 121, 23))
        self.gCodeButton.setObjectName("gCodeButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 620, 781, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.receivedLabel = QtWidgets.QLabel(self.centralwidget)
        self.receivedLabel.setGeometry(QtCore.QRect(9, 236, 63, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.receivedLabel.setFont(font)
        self.receivedLabel.setObjectName("receivedLabel")
        self.interface_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.interface_2.setGeometry(QtCore.QRect(9, 38, 651, 192))
        self.interface_2.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.interface_2.setObjectName("interface_2")
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(9, 258, 791, 351))
        self.output.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.output.setObjectName("output")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(9, 9, 75, 23))
        self.startButton.setStyleSheet("background-color: rgba(17, 255, 25, 100);")
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.stopButton.setStyleSheet("background-color: rgba(255, 0, 0, 100);")
        self.stopButton.setObjectName("stopButton")
        self.originButton = QtWidgets.QPushButton(self.centralwidget)
        self.originButton.setGeometry(QtCore.QRect(680, 70, 121, 23))
        self.originButton.setObjectName("originButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 650, 131, 20))
        self.label.setObjectName("label")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        self.output.setReadOnly(True)
        self.output.setOverwriteMode(False)
        self.interface_2.setReadOnly(True)
        self.interface_2.setOverwriteMode(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GCodeSender"))
        self.gCodeButton.setText(_translate("MainWindow", "Send Gcode"))
        self.receivedLabel.setText(_translate("MainWindow", " Received"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.originButton.setText(_translate("MainWindow", "Go origin"))
        self.label.setText(_translate("MainWindow", "antoine.blaud@gmail.com"))
