# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\antoi\Documents\GitHub\Arduino\ui\com.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_comWIndows(object):
    def setupUi(self, comWIndows):
        comWIndows.setObjectName("comWIndows")
        comWIndows.resize(335, 556)
        comWIndows.setMinimumSize(QtCore.QSize(335, 553))
        comWIndows.setMaximumSize(QtCore.QSize(335, 556))
        self.centralwidget = QtWidgets.QWidget(comWIndows)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        comWIndows.setCentralWidget(self.centralwidget)

        self.retranslateUi(comWIndows)
        QtCore.QMetaObject.connectSlotsByName(comWIndows)

    def retranslateUi(self, comWIndows):
        _translate = QtCore.QCoreApplication.translate
        comWIndows.setWindowTitle(_translate("comWIndows", "COM_PORT"))
        self.pushButton.setText(_translate("comWIndows", "Open "))
