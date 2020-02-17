# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(90, 10, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 13, 47, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 53, 47, 20))
        self.label_2.setObjectName("label_2")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(90, 50, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 261, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 261, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        self.menuFirst_Test_Window = QtWidgets.QMenu(self.menubar)
        self.menuFirst_Test_Window.setObjectName("menuFirst_Test_Window")
        self.menuversion = QtWidgets.QMenu(self.menubar)
        self.menuversion.setObjectName("menuversion")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFirst_Test_Window.menuAction())
        self.menubar.addAction(self.menuversion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dateTimeEdit, self.dateTimeEdit_2)
        MainWindow.setTabOrder(self.dateTimeEdit_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "StartTime"))
        self.label_2.setText(_translate("MainWindow", "End Time"))
        self.pushButton.setText(_translate("MainWindow", "Check Elapsed"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
        self.menuFirst_Test_Window.setTitle(_translate("MainWindow", "Help"))
        self.menuversion.setTitle(_translate("MainWindow", "version"))
