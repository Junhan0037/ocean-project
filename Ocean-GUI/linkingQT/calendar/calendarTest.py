# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import pandas as pd
import statsmodels.api as sm
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QDate



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class MyMain(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calendarWidget.clicked.connect(self.__cal_clicked)

    @pyqtSlot(QDate)
    def __cal_clicked(self, ddate):
        print("-- calendar clicked.....")
        print(ddate.toString())
        tmp_date = str(ddate.toPyDate())
        tmp2 = tmp_date.split("-")
        ddate2 = "".join(tmp2)
        print(tmp_date)
        print(ddate2)
        print("월 = " + str(self.calendarWidget.monthShown()))
        print("년 = " + str(self.calendarWidget.yearShown()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyMain()
    myWindow.show()
    sys.exit(app.exec_())
