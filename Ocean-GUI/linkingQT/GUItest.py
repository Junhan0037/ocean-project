# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_data_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import pandas as pd
import statsmodels.api as sm
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import *
from pandas import DataFrame


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 602)

        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 602)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(650, 600))
        Dialog.setMaximumSize(QtCore.QSize(650, 602))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 11, 620, 580))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(620, 580))
        self.tabWidget.setMaximumSize(QtCore.QSize(620, 580))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(600, 521))
        self.scrollArea.setMaximumSize(QtCore.QSize(554, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.DissolvedOxygen_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.DissolvedOxygen_checkBox.setText("")
        self.DissolvedOxygen_checkBox.setObjectName("DissolvedOxygen_checkBox")
        self.gridLayout.addWidget(self.DissolvedOxygen_checkBox, 0, 5, 1, 1)
        self.NitrousAcidNitrogen_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.NitrousAcidNitrogen_checkBox.setText("")
        self.NitrousAcidNitrogen_checkBox.setObjectName("NitrousAcidNitrogen_checkBox")
        self.gridLayout.addWidget(self.NitrousAcidNitrogen_checkBox, 0, 9, 1, 1)
        self.SilicicAcidSilicon_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.SilicicAcidSilicon_checkBox.setText("")
        self.SilicicAcidSilicon_checkBox.setObjectName("SilicicAcidSilicon_checkBox")
        self.gridLayout.addWidget(self.SilicicAcidSilicon_checkBox, 0, 13, 1, 1)
        self.NitricAcidNitrogen_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.NitricAcidNitrogen_checkBox.setText("")
        self.NitricAcidNitrogen_checkBox.setObjectName("NitricAcidNitrogen_checkBox")
        self.gridLayout.addWidget(self.NitricAcidNitrogen_checkBox, 0, 11, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.PhosphatePhosphorus_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.PhosphatePhosphorus_checkBox.setText("")
        self.PhosphatePhosphorus_checkBox.setObjectName("PhosphatePhosphorus_checkBox")
        self.gridLayout.addWidget(self.PhosphatePhosphorus_checkBox, 0, 7, 1, 1)
        self.WaterTemp_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.WaterTemp_checkBox.setText("")
        self.WaterTemp_checkBox.setObjectName("WaterTemp_checkBox")
        self.gridLayout.addWidget(self.WaterTemp_checkBox, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 6, 1, 1)
        self.Salinity_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Salinity_checkBox.setText("")
        self.Salinity_checkBox.setObjectName("Salinity_checkBox")
        self.gridLayout.addWidget(self.Salinity_checkBox, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 10, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 12, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 8, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        self.All_Data_read_csv_Pushbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.All_Data_read_csv_Pushbutton.setMinimumSize(QtCore.QSize(0, 40))
        self.All_Data_read_csv_Pushbutton.setObjectName("All_Data_read_csv_Pushbutton")
        self.gridLayout_2.addWidget(self.All_Data_read_csv_Pushbutton, 0, 1, 2, 1)
        self.All_Data_read_csv_TextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.All_Data_read_csv_TextEdit.setEnabled(False)
        self.All_Data_read_csv_TextEdit.setObjectName("All_Data_read_csv_TextEdit")
        self.gridLayout_2.addWidget(self.All_Data_read_csv_TextEdit, 3, 0, 1, 3)
        self.LoadFile_PushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.LoadFile_PushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.LoadFile_PushButton.setObjectName("LoadFile_PushButton")
        self.gridLayout_2.addWidget(self.LoadFile_PushButton, 0, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.All_Data_read_csv_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.All_Data_read_csv_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.All_Data_read_csv_lineEdit.setObjectName("All_Data_read_csv_lineEdit")
        self.gridLayout_2.addWidget(self.All_Data_read_csv_lineEdit, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_10.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy)
        self.scrollArea_5.setMinimumSize(QtCore.QSize(600, 521))
        self.scrollArea_5.setMaximumSize(QtCore.QSize(554, 521))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.scrollAreaWidgetContents_5)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_11.addWidget(self.label_27)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Area_EestSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_EestSea_Cbox_2.setObjectName("Area_EestSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_EestSea_Cbox_2)
        self.Area_WestSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_WestSea_Cbox_2.setObjectName("Area_WestSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_WestSea_Cbox_2)
        self.Area_SouthSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_SouthSea_Cbox_2.setObjectName("Area_SouthSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_SouthSea_Cbox_2)
        self.Area_EastChinaSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_EastChinaSea_Cbox_2.setObjectName("Area_EastChinaSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_EastChinaSea_Cbox_2)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.theSeasPage_temp_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_temp_EditLine.setObjectName("theSeasPage_temp_EditLine")
        self.verticalLayout_2.addWidget(self.theSeasPage_temp_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.theSeasPage_Sal_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Sal_EditLine.setObjectName("theSeasPage_Sal_EditLine")
        self.verticalLayout_3.addWidget(self.theSeasPage_Sal_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.theSeasPage_DisOxy_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_DisOxy_EditLine.setObjectName("theSeasPage_DisOxy_EditLine")
        self.verticalLayout_4.addWidget(self.theSeasPage_DisOxy_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.theSeasPage_Phos_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Phos_EditLine.setObjectName("theSeasPage_Phos_EditLine")
        self.verticalLayout_5.addWidget(self.theSeasPage_Phos_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.theSeasPage_Nitrous_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Nitrous_EditLine.setObjectName("theSeasPage_Nitrous_EditLine")
        self.verticalLayout_8.addWidget(self.theSeasPage_Nitrous_EditLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.theSeasPage_Nitric_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Nitric_EditLine.setObjectName("theSeasPage_Nitric_EditLine")
        self.verticalLayout_7.addWidget(self.theSeasPage_Nitric_EditLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.theSeasPage_Sas_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Sas_EditLine.setObjectName("theSeasPage_Sas_EditLine")
        self.verticalLayout_6.addWidget(self.theSeasPage_Sas_EditLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.Page2Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.Page2Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Page2Button.setObjectName("Page2Button")
        self.horizontalLayout_4.addWidget(self.Page2Button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.Calendar_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_5)
        self.Calendar_textEdit.setEnabled(False)
        self.Calendar_textEdit.setObjectName("Calendar_textEdit")
        self.gridLayout_5.addWidget(self.Calendar_textEdit, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy)
        self.scrollArea_6.setMinimumSize(QtCore.QSize(600, 521))
        self.scrollArea_6.setMaximumSize(QtCore.QSize(554, 521))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName("label_26")
        self.gridLayout_16.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_16.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_23.setObjectName("label_23")
        self.gridLayout_16.addWidget(self.label_23, 0, 2, 1, 1)
        self.PredictPage_3ea_pridet_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_pridet_Button.setObjectName("PredictPage_3ea_pridet_Button")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_pridet_Button, 0, 3, 2, 1)
        self.PredictPage_3ea_Temp_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_Temp_Edit.setObjectName("PredictPage_3ea_Temp_Edit")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_Temp_Edit, 1, 0, 1, 1)
        self.PredictPage_3ea_Sal_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_Sal_Edit.setObjectName("PredictPage_3ea_Sal_Edit")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_Sal_Edit, 1, 1, 1, 1)
        self.PredictPage_3ea_DisOxy_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_DisOxy_Edit.setObjectName("PredictPage_3ea_DisOxy_Edit")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_DisOxy_Edit, 1, 2, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.PredictPage_3ea_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_textEdit.setObjectName("PredictPage_3ea_textEdit")
        self.gridLayout_17.addWidget(self.PredictPage_3ea_textEdit, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_21.setObjectName("label_21")
        self.gridLayout_18.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout_18.addWidget(self.label_24, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_25.setObjectName("label_25")
        self.gridLayout_18.addWidget(self.label_25, 0, 3, 1, 1)
        self.PredictPage_4ea_pridet_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_pridet_Button.setObjectName("PredictPage_4ea_pridet_Button")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_pridet_Button, 0, 4, 2, 1)
        self.PredictPage_4ea_Phos_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Phos_Edit.setObjectName("PredictPage_4ea_Phos_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Phos_Edit, 1, 0, 1, 1)
        self.PredictPage_4ea_Nitrous_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Nitrous_Edit.setObjectName("PredictPage_4ea_Nitrous_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Nitrous_Edit, 1, 1, 1, 1)
        self.PredictPage_4ea_Nitric_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Nitric_Edit.setObjectName("PredictPage_4ea_Nitric_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Nitric_Edit, 1, 2, 1, 1)
        self.PredictPage_4ea_Sas_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Sas_Edit.setObjectName("PredictPage_4ea_Sas_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Sas_Edit, 1, 3, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.PredictPage_4ea_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_textEdit.setObjectName("PredictPage_4ea_textEdit")
        self.gridLayout_19.addWidget(self.PredictPage_4ea_textEdit, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.PredictPage_7ea_Phos_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Phos_Edit.setObjectName("PredictPage_7ea_Phos_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Phos_Edit, 3, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_54.setObjectName("label_54")
        self.gridLayout_20.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_53.setObjectName("label_53")
        self.gridLayout_20.addWidget(self.label_53, 0, 1, 1, 1)
        self.PredictPage_7ea_Sal_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Sal_Edit.setObjectName("PredictPage_7ea_Sal_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Sal_Edit, 1, 1, 1, 1)
        self.PredictPage_7ea_DisOxy_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_DisOxy_Edit.setObjectName("PredictPage_7ea_DisOxy_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_DisOxy_Edit, 1, 2, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_59.setObjectName("label_59")
        self.gridLayout_20.addWidget(self.label_59, 2, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_55.setObjectName("label_55")
        self.gridLayout_20.addWidget(self.label_55, 0, 2, 1, 1)
        self.PredictPage_7ea_pridet_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_pridet_Button.setObjectName("PredictPage_7ea_pridet_Button")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_pridet_Button, 0, 3, 2, 1)
        self.PredictPage_7ea_Temp_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Temp_Edit.setObjectName("PredictPage_7ea_Temp_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Temp_Edit, 1, 0, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_57.setObjectName("label_57")
        self.gridLayout_20.addWidget(self.label_57, 2, 1, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_56.setObjectName("label_56")
        self.gridLayout_20.addWidget(self.label_56, 2, 2, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_58.setObjectName("label_58")
        self.gridLayout_20.addWidget(self.label_58, 2, 3, 1, 1)
        self.PredictPage_7ea_Nitric_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Nitric_Edit.setObjectName("PredictPage_7ea_Nitric_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Nitric_Edit, 3, 2, 1, 1)
        self.PredictPage_7ea_Sas_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Sas_Edit.setObjectName("PredictPage_7ea_Sas_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Sas_Edit, 3, 3, 1, 1)
        self.PredictPage_7ea_Nitrous_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Nitrous_Edit.setObjectName("PredictPage_7ea_Nitrous_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Nitrous_Edit, 3, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.PredictPage_7ea_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_textEdit.setObjectName("PredictPage_7ea_textEdit")
        self.gridLayout_21.addWidget(self.PredictPage_7ea_textEdit, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_21, 2, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_23.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(600, 519))
        self.label_2.setMaximumSize(QtCore.QSize(554, 519))
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "염분"))
        self.label_6.setText(_translate("Dialog", "용존산소"))
        self.label_9.setText(_translate("Dialog", "인산염인"))
        self.label_10.setText(_translate("Dialog", "질산질소"))
        self.label_12.setText(_translate("Dialog", "규산규소"))
        self.label_4.setText(_translate("Dialog", "수온"))
        self.label_11.setText(_translate("Dialog", "아질산질소"))
        self.All_Data_read_csv_Pushbutton.setText(_translate("Dialog", "출력하기"))
        self.LoadFile_PushButton.setText(_translate("Dialog", "불러오기"))
        self.label.setText(_translate("Dialog", "csv파일을 입력하시오."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "All_Data"))
        self.label_27.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_27.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">&lt;해역을 선택하여 주세요&gt;</span></p></body></html>"))
        self.Area_EestSea_Cbox_2.setText(_translate("Dialog", "동해"))
        self.Area_WestSea_Cbox_2.setText(_translate("Dialog", "서해"))
        self.Area_SouthSea_Cbox_2.setText(_translate("Dialog", "남해"))
        self.Area_EastChinaSea_Cbox_2.setText(_translate("Dialog", "동중국해"))
        self.label_3.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">&lt; 해달 날짜의 평균 요소 값 &gt;</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "수온"))
        self.label_13.setText(_translate("Dialog", "염분"))
        self.label_14.setText(_translate("Dialog", "용존산소"))
        self.label_18.setText(_translate("Dialog", "인산염인"))
        self.label_16.setText(_translate("Dialog", "아질산질소"))
        self.label_15.setText(_translate("Dialog", "질산질소"))
        self.label_17.setText(_translate("Dialog", "규산규소"))
        self.Page2Button.setText(_translate("Dialog", "          버튼         "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Calender"))
        self.label_26.setText(_translate("Dialog", "수온"))
        self.label_20.setText(_translate("Dialog", "염분"))
        self.label_23.setText(_translate("Dialog", "용존산소"))
        self.PredictPage_3ea_pridet_Button.setText(_translate("Dialog", "확인"))
        self.label_21.setText(_translate("Dialog", "인산염인"))
        self.label_24.setText(_translate("Dialog", "아질산질소"))
        self.label_22.setText(_translate("Dialog", "질산질소"))
        self.label_25.setText(_translate("Dialog", "규산규소"))
        self.PredictPage_4ea_pridet_Button.setText(_translate("Dialog", "확인"))
        self.label_54.setText(_translate("Dialog", "수온"))
        self.label_53.setText(_translate("Dialog", "염분"))
        self.label_59.setText(_translate("Dialog", "인산염인"))
        self.label_55.setText(_translate("Dialog", "용존산소"))
        self.PredictPage_7ea_pridet_Button.setText(_translate("Dialog", "확인"))
        self.label_57.setText(_translate("Dialog", "아질산질소"))
        self.label_56.setText(_translate("Dialog", "질산질소"))
        self.label_58.setText(_translate("Dialog", "규산규소"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Predict"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-family:\'휴먼명조\'; font-size:14pt;\">정선해양관측자료를 통해본 유해적조</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">김준한 · 강민석 · 이동현 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">신라대학교 빅데이터연구실</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\'; font-size:11pt;\">The toxic red tide, ocean observation information through the Choice</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">Kim-Jun Han · Gang-Min Seok · Lee-Dong Hyeon</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">Korea Silla Univercity BigData Lab</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">E-mail : axzswq@sillain.ac.kr</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">적조현상은 우리의 생태계나 인류에게 위협적인 환경문제 중 하나이다. <p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">본 논문에서 저자들은 해양요인들 중 정선해양관측정보에서 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">수온, 염분, 용존산소, 인산염인, 아질산질소, 질산질소, 규산수소의 7개의 요소를 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">python의 pandas 라이브러리를 이용하여서 데이터 추출, 과거적조발생자료를 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">국립수산과학원에서 웹 크롤링한 후에 자료들과 통합하여서 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">영향력을 제공하는 요소를 로지스틱 회귀분석 방식으로 분석했다. </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">2000~2017년 정보들을 대상으로 진행하였다.</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">본 논문을 통해 해양에 적조가 생기는 이유를 정밀하게 발견하고 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">적조발생을 예방하며 생태계와 학술계에 도움이 되기를 희망한다.</span></p><p align=\"center\"><br/></p><p align=\"center\">담당 교수)윤홍원 교수님</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Epilogue"))


'''
class MainGUI(QtWidgets.QMainWindow,Ui_Dialog)
상속 받은 클래스가 
'''


class MainGUI(QtWidgets.QMainWindow, Ui_Dialog):
    # page2에 필요한 전역 변수
    page2_date = ""  # 날짜
    sea_area = None  # 해역 선택

    my_dict = {"Temperature": ['0'], "Salinity": ['0'], "Dissolved Oxygen": ['0'],
               "Phosphate Phosphorus": ['0'], "Nitrous Acid Nitrogen": ['0'], "Nitric Acid Nitrogen": ['0'],
               "Silicic Acid Silicon": ['0']}


class MainGUI(QtWidgets.QMainWindow, Ui_Dialog):
    my_dict = {"Temperature": ['0'], "Salinity": ['0'], "Dissolved Oxygen": ['0'],
               "Phosphate Phosphorus": ['0'], "Nitrous Acid Nitrogen": ['0'], "Nitric Acid Nitrogen": ['0'],
               "Silicic Acid Silicon": ['0']}
    check_df = pd.DataFrame(my_dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 해당 버튼 클릭 시 해당 함수호출을 선언
        # 1page 버튼
        # 불러오기 버튼
        self.LoadFile_PushButton.clicked.connect(self.get_file_name)
        # '출력하기'버튼
        self.All_Data_read_csv_Pushbutton.clicked.connect(
            lambda state, button=self.All_Data_read_csv_Pushbutton: self.All_Data_ReadClicked(state,
                                                                                              button))  # 1page csv 버튼

        self.Page2Button.clicked.connect(self.Page2PredictpushButton)  # 2page 날짜별 해역별 예측하기 버튼

        # Able lineEdit
        self.WaterTemp_checkBox.stateChanged.connect(lambda: self.WaterTemp_state(self))
        self.Salinity_checkBox.stateChanged.connect(lambda: self.Salinity_state(self))
        self.DissolvedOxygen_checkBox.stateChanged.connect(lambda: self.DissolvedOxygen_state(self))
        self.PhosphatePhosphorus_checkBox.stateChanged.connect(lambda: self.PhosphatePhosphorus_state(self))
        self.NitrousAcidNitrogen_checkBox.stateChanged.connect(lambda: self.NitrousAcidNitrogen_state(self))
        self.NitricAcidNitrogen_checkBox.stateChanged.connect(lambda: self.NitricAcidNitrogen_state(self))
        self.SilicicAcidSilicon_checkBox.stateChanged.connect(lambda: self.SilicicAcidSilicon_state(self))

        # Page2
        self.calendarWidget.clicked.connect(self.__cal_clicked)
        self.Area_EestSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 동해
        self.Area_WestSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 서해
        self.Area_SouthSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 남해
        self.Area_EastChinaSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 동중국해

        # Page3
        self.PredictPage_3ea_pridet_Button.clicked.connect(self.Pridict3eaButton)
        self.PredictPage_4ea_pridet_Button.clicked.connect(self.Pridict4eaButton)
        self.PredictPage_7ea_pridet_Button.clicked.connect(self.Pridict7eaButton)

    # 불러오기 기능
    def get_file_name(self):
        filename = QFileDialog.getOpenFileName()
        self.All_Data_read_csv_lineEdit.setText(filename[0])

    def All_Data_ReadClicked(self, state, button):

        # lineEdit에 write한 csv파일을 읽어들임
        # header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
        data_frame = pd.read_csv(str(self.All_Data_read_csv_lineEdit.text()), header=0)
        # 종속변수로 선언
        dependent_variable = data_frame['On/Off']

        # 체크된 요소 확인
        print('##############################################################')
        i = 0
        checked_columns = []
        for temp in MainGUI.check_df.iloc[0][:]:
            if temp == 1:
                checked_columns.append(MainGUI.check_df.columns[i])
            i += 1
        print(checked_columns)

        print('##############################################################')

        # 독립변수로 선언
        independent_variables = data_frame[checked_columns]
        # 입력변수에 전체 값이 1인 열을 추가
        independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
        # 로지스틱 회귀모형에 피팅 (NaN행 무시)
        logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

        print('WOW 1')

        # 회귀계수 해석
        def inverse_logit(model_formula):
            from math import exp
            return (1.0 / (1.0 + exp(-model_formula)))

        print(str(logit_model.summary()))

        # 결과창에 출력 (아직 안됌)
        # self.All_Data_read_csv_TextEdit.setText(str(logit_model.summary()))

        ####################################################################### 7.13 여기까지 성공!

        print('0단계')
        # 평균값을 입력시 발생확률
        at_means = float(logit_model.params[0])

        for i in range(0, len(checked_columns)):
            print(checked_columns[i])
            at_means = at_means + float(logit_model.params[i + 1]) * float(data_frame[checked_columns[i]].mean())
        print("첫 for문 통과")
        print("if문 나옴")

        # 7가지 요소들의 평균 값을 입력시 적조발생 확률
        probability = (inverse_logit(at_means)) * 100
        self.All_Data_read_csv_TextEdit.setText(
            str(logit_model.summary()) + "\n" + str(checked_columns) + " 요소들의 평균 값을 입력시 적조 발생 확률 : \n" + str(
                round(probability, 3)) + "%")

    # 체크박스 체크시 LineEdit에 Write 가능하게 만들었습니다.
    # WaterTemp_state라는 함수를 정의
    # setDisable(Ture)는 사용을 못하게 만드는 명령어.
    def WaterTemp_state(self, state):
        if self.WaterTemp_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Temperature'] = 1
        else:
            MainGUI.check_df.ix[0]['Temperature'] = 0

    def Salinity_state(self, state):
        if self.Salinity_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Salinity'] = 1
        else:
            MainGUI.check_df.ix[0]['Salinity'] = 0

    def DissolvedOxygen_state(self, state):
        if self.DissolvedOxygen_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Dissolved Oxygen'] = 1
        else:
            MainGUI.check_df.ix[0]['Dissolved Oxygen'] = 0

    def PhosphatePhosphorus_state(self, state):
        if self.PhosphatePhosphorus_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Phosphate Phosphorus'] = 1
        else:
            MainGUI.check_df.ix[0]['Phosphate Phosphorus'] = 0

    def NitrousAcidNitrogen_state(self, state):
        if self.NitrousAcidNitrogen_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Nitrous Acid Nitrogen'] = 1
        else:
            MainGUI.check_df.ix[0]['Nitrous Acid Nitrogen'] = 0

    def NitricAcidNitrogen_state(self, state):
        if self.NitricAcidNitrogen_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Nitric Acid Nitrogen'] = 1
        else:
            MainGUI.check_df.ix[0]['Nitric Acid Nitrogen'] = 0

    def SilicicAcidSilicon_state(self, state):
        if self.SilicicAcidSilicon_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Silicic Acid Silicon'] = 1
        else:
            MainGUI.check_df.ix[0]['Silicic Acid Silicon'] = 0

    '''
    def onePageSearchpushButton(self):
        #self.textEdit.toPlainText() : GUI에 있는 단어를 가져오는 역할.
        print(self.WaterTempLineEdit.text()) #1page 수온
        print(self.SalinitylineEdit.text()) #1page 염분
        print(self.DissolvedOxygenlineEdit.text())  #1page 용존산소
        print(self.PhosphatePhosphoruslineEdit.text()) #1apge 인산염인
        print(self.NitrousAcidNitrogenlineEdit.text()) #1page 아질산질소
        print(self.NitricAcidNitrogenlineEdit.text()) #1page 질산질소
        print(self.SilicicAcidSiliconlineEdit.text()) #1page 규산규소
    '''

    # 2page에 해역을 선택하는 부분입니다.
    def Area_EestSea_state(self):
        if self.Area_EestSea_Cbox_2.isChecked():
            self.sea_area = "동해"
            print(self.sea_area)
        elif self.Area_WestSea_Cbox_2.isChecked():
            self.sea_area = "서해"
            print(self.sea_area)
        elif self.Area_SouthSea_Cbox_2.isChecked():
            self.sea_area = "남해"
            print(self.sea_area)
        elif self.Area_EastChinaSea_Cbox_2.isChecked():
            self.sea_area = "동중국해"
            print(self.sea_area)

    '''
    def Area_WestSea_state(self, state):


    def Area_SouthSea_state(self, state):


    def Area_EastChinaSea_state(self, state):
    '''

    '''
    Area_EestSea_state
    Area_WestSea_state
    Area_SouthSea_state
    Area_EastChinaSea_state


    self.Area_EestSea_Cbox_2.stateChanged.connect(lambda: self.Area_EestSea_state(self))  # 동해
    self.Area_WestSea_Cbox_2.stateChanged.connect(lambda: self.Area_WestSea_state(self))  # 서해
    self.Area_SouthSea_Cbox_2.stateChanged.connect(lambda: self.Area_SouthSea_state(self))  # 남해
    self.Area_EastChinaSea_Cbox_2.stateChanged.connect(lambda: self.Area_EastChinaSea_state(self))  # 동중국해
    '''

    @pyqtSlot(QDate)
    def __cal_clicked(self, ddate):
        print("-- calendar clicked.....")
        print(ddate.toString())
        tmp_date = str(ddate.toPyDate())
        tmp2 = tmp_date.split("-")
        print(tmp2[0])
        print(tmp2[1])
        print(tmp2[2])
        ddate2 = "".join(tmp2)
        print(tmp_date)
        print(ddate2)
        print("월 = " + str(self.calendarWidget.monthShown()))
        print("년 = " + str(self.calendarWidget.yearShown()))

        self.page2_date = tmp_date  # 전역 클래스의

    def Page2PredictpushButton(self):  # page2의 버튼 누르면 일어나는 현상
        msgbox = QtWidgets.QMessageBox(self)
        tab2_dataframe = pd.read_csv("tab2.csv", header=0, encoding='cp949')
        i_df = pd.DataFrame()

        # 멀티 인덱싱 하여서 groupby 메커니즘 사용
        grouped_ocean_data = tab2_dataframe.groupby(['Sea_area', 'Observation Date'])

        try:
            # 해역 인덱스와 날짜 인덱스의 값이 일치하는 그룹만 불러옵니다.
            i_df = grouped_ocean_data.get_group((self.sea_area, self.page2_date))
            # 위에서 정제된 그룹의 평균을 구합니다.
            i_df = i_df.groupby(['Sea_area', 'Observation Date']).mean()

            # 문자열을 editline이여서 설정형식으로 해주었습니다. 문제는 문자열만 되기에 소수점 3자리 기준으로 문자열 변환
            # 하여서 출력해주었습니다.
            self.theSeasPage_temp_EditLine.setText(str(round(i_df.iloc[0][0], 3)))
            self.theSeasPage_Sal_EditLine.setText(str(round(i_df.iloc[0][1], 3)))
            self.theSeasPage_DisOxy_EditLine.setText(str(round(i_df.iloc[0][2], 3)))
            self.theSeasPage_Phos_EditLine.setText(str(round(i_df.iloc[0][3], 3)))
            self.theSeasPage_Nitrous_EditLine.setText(str(round(i_df.iloc[0][4], 3)))
            self.theSeasPage_Nitric_EditLine.setText(str(round(i_df.iloc[0][5], 3)))
            self.theSeasPage_Sas_EditLine.setText(str(round(i_df.iloc[0][6], 3)))
        except KeyError:  # 912줄에 데이터값이 그룹이 안될경우 이 에러가 뜹니다
            self.Calendar_textEdit.setText("이 날짜에는 데이터가 값이 없습니다.\n 2000~2017년 사이에 지정해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '이 날짜에는 데이터가 값이 없습니다.\n 2000~2017년 사이에 지정해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

            print("이 해역의 이 날짜에는 데이터가 값이 없습니다.")
        except IndexError:  # 문자열 입력 도중에 넣을 데이터 값이 없어서도 안 됩니다.
            self.Calendar_textEdit.setText("이 날짜에는 데이터 값이 없어서 출력도 안 됩니다. \n 2000~2017년 사이에 지정해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '이 날짜에는 데이터 값이 없어서 출력도 안 됩니다.\n 2000~2017년 사이에 지정해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

            print("이 해역의 이 날짜에는 데이터 값이 없어서 출력도 안 됩니다. ㅠㅠ")

    def Pridict3eaButton(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:
            data_frame = pd.read_csv('tab3.csv', header=0)
            dependent_variable = data_frame['On/Off']
            independent_variables = data_frame[['Temperature', 'Salinity', 'Dissolved Oxygen']]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

            input_data1 = float(self.PredictPage_3ea_Temp_Edit.text())
            input_data2 = float(self.PredictPage_3ea_Sal_Edit.text())
            input_data3 = float(self.PredictPage_3ea_DisOxy_Edit.text())

            # 앞 두개의 데이터는 원래의 데이터값을 그대로, 입력받은 값을 배열로 생성
            input_data = np.array([[14.62, 34.19, 5.63], [14.71, 34.19, 5.61],
                                   [input_data1, input_data2, input_data3]])
            df = pd.DataFrame(data=input_data, columns=[independent_variables])

            # 최소 데이터 3개 이상이어야 예측가능
            new_observations = df.ix[data_frame.index.isin(range(3)), independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 4) for score in y_predicted]

            # 예상 확률 출력
            self.PredictPage_3ea_textEdit.setText('적조 발생 확률 : ' + str(round(y_predicted_rounded[2] * 100, 4)) + '%')


        except ValueError:
            self.PredictPage_3ea_textEdit.setText("데이터 (실수값)를 입력해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '데이터 (실수값)를 입력해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

    def Pridict4eaButton(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:

            data_frame = pd.read_csv('tab3.csv', header=0)
            dependent_variable = data_frame['On/Off']
            independent_variables = data_frame[
                ['Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

            input_data1 = float(self.PredictPage_4ea_Phos_Edit.text())
            input_data2 = float(self.PredictPage_4ea_Nitrous_Edit.text())
            input_data3 = float(self.PredictPage_4ea_Nitric_Edit.text())
            input_data4 = float(self.PredictPage_4ea_Sas_Edit.text())

            # 앞 두개의 데이터는 원래의 데이터값을 그대로, 입력받은 값을 배열로 생성
            input_data = np.array([[0.44, 0.68, 7.56, 8.33], [0.41, 0.63, 7.42, 8.13],
                                   [input_data1, input_data2, input_data3, input_data4]])
            df = pd.DataFrame(data=input_data, columns=[independent_variables])

            # 최소 데이터 3개 이상이어야 예측가능
            new_observations = df.ix[data_frame.index.isin(range(3)), independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 4) for score in y_predicted]

            # 예상 확률 출력
            self.PredictPage_4ea_textEdit.setText('적조 발생 확률 : ' + str(round(y_predicted_rounded[2] * 100, 4)) + '%')
        except ValueError:
            self.PredictPage_4ea_textEdit.setText("데이터 값을 입력해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '데이터 값을 입력해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

    def Pridict7eaButton(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:

            data_frame = pd.read_csv('tab3.csv', header=0)
            dependent_variable = data_frame['On/Off']
            independent_variables = data_frame[
                ['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen',
                 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

            input_data1 = float(self.PredictPage_7ea_Temp_Edit.text())
            input_data2 = float(self.PredictPage_7ea_Sal_Edit.text())
            input_data3 = float(self.PredictPage_7ea_DisOxy_Edit.text())
            input_data4 = float(self.PredictPage_7ea_Phos_Edit.text())
            input_data5 = float(self.PredictPage_7ea_Nitrous_Edit.text())
            input_data6 = float(self.PredictPage_7ea_Nitric_Edit.text())
            input_data7 = float(self.PredictPage_7ea_Sas_Edit.text())

            # 앞 두개의 데이터는 원래의 데이터값을 그대로, 입력받은 값을 배열로 생성
            input_data = np.array(
                [[14.62, 34.19, 5.63, 0.44, 0.68, 7.56, 8.33], [14.91, 34.21, 5.5, 0.41, 0.63, 7.42, 8.13],
                 [input_data1, input_data2, input_data3, input_data4, input_data5, input_data6, input_data7]])
            df = pd.DataFrame(data=input_data, columns=[independent_variables])

            # 최소 데이터 3개 이상이어야 예측가능
            new_observations = df.ix[data_frame.index.isin(range(3)), independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 4) for score in y_predicted]

            # 예상 확률 출력
            self.PredictPage_7ea_textEdit.setText('적조 발생 확률 : ' + str(round(y_predicted_rounded[2] * 100, 4)) + '%')

        except ValueError:
            self.PredictPage_7ea_textEdit.setText("데이터 값을 입력해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '데이터 값을 입력해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainGUI()
    myWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_data_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
import pandas as pd
import statsmodels.api as sm
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import *
from pandas import DataFrame


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 602)

        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 602)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(650, 600))
        Dialog.setMaximumSize(QtCore.QSize(650, 602))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 11, 620, 580))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(620, 580))
        self.tabWidget.setMaximumSize(QtCore.QSize(620, 580))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(600, 521))
        self.scrollArea.setMaximumSize(QtCore.QSize(554, 521))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.DissolvedOxygen_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.DissolvedOxygen_checkBox.setText("")
        self.DissolvedOxygen_checkBox.setObjectName("DissolvedOxygen_checkBox")
        self.gridLayout.addWidget(self.DissolvedOxygen_checkBox, 0, 5, 1, 1)
        self.NitrousAcidNitrogen_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.NitrousAcidNitrogen_checkBox.setText("")
        self.NitrousAcidNitrogen_checkBox.setObjectName("NitrousAcidNitrogen_checkBox")
        self.gridLayout.addWidget(self.NitrousAcidNitrogen_checkBox, 0, 9, 1, 1)
        self.SilicicAcidSilicon_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.SilicicAcidSilicon_checkBox.setText("")
        self.SilicicAcidSilicon_checkBox.setObjectName("SilicicAcidSilicon_checkBox")
        self.gridLayout.addWidget(self.SilicicAcidSilicon_checkBox, 0, 13, 1, 1)
        self.NitricAcidNitrogen_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.NitricAcidNitrogen_checkBox.setText("")
        self.NitricAcidNitrogen_checkBox.setObjectName("NitricAcidNitrogen_checkBox")
        self.gridLayout.addWidget(self.NitricAcidNitrogen_checkBox, 0, 11, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.PhosphatePhosphorus_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.PhosphatePhosphorus_checkBox.setText("")
        self.PhosphatePhosphorus_checkBox.setObjectName("PhosphatePhosphorus_checkBox")
        self.gridLayout.addWidget(self.PhosphatePhosphorus_checkBox, 0, 7, 1, 1)
        self.WaterTemp_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.WaterTemp_checkBox.setText("")
        self.WaterTemp_checkBox.setObjectName("WaterTemp_checkBox")
        self.gridLayout.addWidget(self.WaterTemp_checkBox, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 6, 1, 1)
        self.Salinity_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Salinity_checkBox.setText("")
        self.Salinity_checkBox.setObjectName("Salinity_checkBox")
        self.gridLayout.addWidget(self.Salinity_checkBox, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 10, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 12, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 8, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        self.All_Data_read_csv_Pushbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.All_Data_read_csv_Pushbutton.setMinimumSize(QtCore.QSize(0, 40))
        self.All_Data_read_csv_Pushbutton.setObjectName("All_Data_read_csv_Pushbutton")
        self.gridLayout_2.addWidget(self.All_Data_read_csv_Pushbutton, 0, 1, 2, 1)
        self.All_Data_read_csv_TextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.All_Data_read_csv_TextEdit.setEnabled(False)
        self.All_Data_read_csv_TextEdit.setObjectName("All_Data_read_csv_TextEdit")
        self.gridLayout_2.addWidget(self.All_Data_read_csv_TextEdit, 3, 0, 1, 3)
        self.LoadFile_PushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.LoadFile_PushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.LoadFile_PushButton.setObjectName("LoadFile_PushButton")
        self.gridLayout_2.addWidget(self.LoadFile_PushButton, 0, 2, 2, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.All_Data_read_csv_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.All_Data_read_csv_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.All_Data_read_csv_lineEdit.setObjectName("All_Data_read_csv_lineEdit")
        self.gridLayout_2.addWidget(self.All_Data_read_csv_lineEdit, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_10.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy)
        self.scrollArea_5.setMinimumSize(QtCore.QSize(600, 521))
        self.scrollArea_5.setMaximumSize(QtCore.QSize(554, 521))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.scrollAreaWidgetContents_5)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_11.addWidget(self.label_27)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Area_EestSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_EestSea_Cbox_2.setObjectName("Area_EestSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_EestSea_Cbox_2)
        self.Area_WestSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_WestSea_Cbox_2.setObjectName("Area_WestSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_WestSea_Cbox_2)
        self.Area_SouthSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_SouthSea_Cbox_2.setObjectName("Area_SouthSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_SouthSea_Cbox_2)
        self.Area_EastChinaSea_Cbox_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_5)
        self.Area_EastChinaSea_Cbox_2.setObjectName("Area_EastChinaSea_Cbox_2")
        self.verticalLayout.addWidget(self.Area_EastChinaSea_Cbox_2)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.theSeasPage_temp_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_temp_EditLine.setObjectName("theSeasPage_temp_EditLine")
        self.verticalLayout_2.addWidget(self.theSeasPage_temp_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.theSeasPage_Sal_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Sal_EditLine.setObjectName("theSeasPage_Sal_EditLine")
        self.verticalLayout_3.addWidget(self.theSeasPage_Sal_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.theSeasPage_DisOxy_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_DisOxy_EditLine.setObjectName("theSeasPage_DisOxy_EditLine")
        self.verticalLayout_4.addWidget(self.theSeasPage_DisOxy_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.theSeasPage_Phos_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Phos_EditLine.setObjectName("theSeasPage_Phos_EditLine")
        self.verticalLayout_5.addWidget(self.theSeasPage_Phos_EditLine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.theSeasPage_Nitrous_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Nitrous_EditLine.setObjectName("theSeasPage_Nitrous_EditLine")
        self.verticalLayout_8.addWidget(self.theSeasPage_Nitrous_EditLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_7.addWidget(self.label_15)
        self.theSeasPage_Nitric_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Nitric_EditLine.setObjectName("theSeasPage_Nitric_EditLine")
        self.verticalLayout_7.addWidget(self.theSeasPage_Nitric_EditLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.theSeasPage_Sas_EditLine = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.theSeasPage_Sas_EditLine.setObjectName("theSeasPage_Sas_EditLine")
        self.verticalLayout_6.addWidget(self.theSeasPage_Sas_EditLine)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.Page2Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.Page2Button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Page2Button.setObjectName("Page2Button")
        self.horizontalLayout_4.addWidget(self.Page2Button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.Calendar_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_5)
        self.Calendar_textEdit.setEnabled(False)
        self.Calendar_textEdit.setObjectName("Calendar_textEdit")
        self.gridLayout_5.addWidget(self.Calendar_textEdit, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy)
        self.scrollArea_6.setMinimumSize(QtCore.QSize(600, 521))
        self.scrollArea_6.setMaximumSize(QtCore.QSize(554, 521))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 598, 519))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_26.setObjectName("label_26")
        self.gridLayout_16.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_16.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_23.setObjectName("label_23")
        self.gridLayout_16.addWidget(self.label_23, 0, 2, 1, 1)
        self.PredictPage_3ea_pridet_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_pridet_Button.setObjectName("PredictPage_3ea_pridet_Button")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_pridet_Button, 0, 3, 2, 1)
        self.PredictPage_3ea_Temp_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_Temp_Edit.setObjectName("PredictPage_3ea_Temp_Edit")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_Temp_Edit, 1, 0, 1, 1)
        self.PredictPage_3ea_Sal_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_Sal_Edit.setObjectName("PredictPage_3ea_Sal_Edit")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_Sal_Edit, 1, 1, 1, 1)
        self.PredictPage_3ea_DisOxy_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_DisOxy_Edit.setObjectName("PredictPage_3ea_DisOxy_Edit")
        self.gridLayout_16.addWidget(self.PredictPage_3ea_DisOxy_Edit, 1, 2, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.PredictPage_3ea_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_3ea_textEdit.setObjectName("PredictPage_3ea_textEdit")
        self.gridLayout_17.addWidget(self.PredictPage_3ea_textEdit, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_17, 0, 0, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_21.setObjectName("label_21")
        self.gridLayout_18.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_24.setObjectName("label_24")
        self.gridLayout_18.addWidget(self.label_24, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_22.setObjectName("label_22")
        self.gridLayout_18.addWidget(self.label_22, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_25.setObjectName("label_25")
        self.gridLayout_18.addWidget(self.label_25, 0, 3, 1, 1)
        self.PredictPage_4ea_pridet_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_pridet_Button.setObjectName("PredictPage_4ea_pridet_Button")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_pridet_Button, 0, 4, 2, 1)
        self.PredictPage_4ea_Phos_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Phos_Edit.setObjectName("PredictPage_4ea_Phos_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Phos_Edit, 1, 0, 1, 1)
        self.PredictPage_4ea_Nitrous_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Nitrous_Edit.setObjectName("PredictPage_4ea_Nitrous_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Nitrous_Edit, 1, 1, 1, 1)
        self.PredictPage_4ea_Nitric_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Nitric_Edit.setObjectName("PredictPage_4ea_Nitric_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Nitric_Edit, 1, 2, 1, 1)
        self.PredictPage_4ea_Sas_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_Sas_Edit.setObjectName("PredictPage_4ea_Sas_Edit")
        self.gridLayout_18.addWidget(self.PredictPage_4ea_Sas_Edit, 1, 3, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.PredictPage_4ea_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_4ea_textEdit.setObjectName("PredictPage_4ea_textEdit")
        self.gridLayout_19.addWidget(self.PredictPage_4ea_textEdit, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.PredictPage_7ea_Phos_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Phos_Edit.setObjectName("PredictPage_7ea_Phos_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Phos_Edit, 3, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_54.setObjectName("label_54")
        self.gridLayout_20.addWidget(self.label_54, 0, 0, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_53.setObjectName("label_53")
        self.gridLayout_20.addWidget(self.label_53, 0, 1, 1, 1)
        self.PredictPage_7ea_Sal_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Sal_Edit.setObjectName("PredictPage_7ea_Sal_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Sal_Edit, 1, 1, 1, 1)
        self.PredictPage_7ea_DisOxy_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_DisOxy_Edit.setObjectName("PredictPage_7ea_DisOxy_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_DisOxy_Edit, 1, 2, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_59.setObjectName("label_59")
        self.gridLayout_20.addWidget(self.label_59, 2, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_55.setObjectName("label_55")
        self.gridLayout_20.addWidget(self.label_55, 0, 2, 1, 1)
        self.PredictPage_7ea_pridet_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_pridet_Button.setObjectName("PredictPage_7ea_pridet_Button")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_pridet_Button, 0, 3, 2, 1)
        self.PredictPage_7ea_Temp_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Temp_Edit.setObjectName("PredictPage_7ea_Temp_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Temp_Edit, 1, 0, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_57.setObjectName("label_57")
        self.gridLayout_20.addWidget(self.label_57, 2, 1, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_56.setObjectName("label_56")
        self.gridLayout_20.addWidget(self.label_56, 2, 2, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_58.setObjectName("label_58")
        self.gridLayout_20.addWidget(self.label_58, 2, 3, 1, 1)
        self.PredictPage_7ea_Nitric_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Nitric_Edit.setObjectName("PredictPage_7ea_Nitric_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Nitric_Edit, 3, 2, 1, 1)
        self.PredictPage_7ea_Sas_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Sas_Edit.setObjectName("PredictPage_7ea_Sas_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Sas_Edit, 3, 3, 1, 1)
        self.PredictPage_7ea_Nitrous_Edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_Nitrous_Edit.setObjectName("PredictPage_7ea_Nitrous_Edit")
        self.gridLayout_20.addWidget(self.PredictPage_7ea_Nitrous_Edit, 3, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.PredictPage_7ea_textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_6)
        self.PredictPage_7ea_textEdit.setObjectName("PredictPage_7ea_textEdit")
        self.gridLayout_21.addWidget(self.PredictPage_7ea_textEdit, 1, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_21, 2, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_23.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(600, 519))
        self.label_2.setMaximumSize(QtCore.QSize(554, 519))
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "염분"))
        self.label_6.setText(_translate("Dialog", "용존산소"))
        self.label_9.setText(_translate("Dialog", "인산염인"))
        self.label_10.setText(_translate("Dialog", "질산질소"))
        self.label_12.setText(_translate("Dialog", "규산규소"))
        self.label_4.setText(_translate("Dialog", "수온"))
        self.label_11.setText(_translate("Dialog", "아질산질소"))
        self.All_Data_read_csv_Pushbutton.setText(_translate("Dialog", "출력하기"))
        self.LoadFile_PushButton.setText(_translate("Dialog", "불러오기"))
        self.label.setText(_translate("Dialog", "csv파일을 입력하시오."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "All_Data"))
        self.label_27.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_27.setText(_translate("Dialog",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">&lt;해역을 선택하여 주세요&gt;</span></p></body></html>"))
        self.Area_EestSea_Cbox_2.setText(_translate("Dialog", "동해"))
        self.Area_WestSea_Cbox_2.setText(_translate("Dialog", "서해"))
        self.Area_SouthSea_Cbox_2.setText(_translate("Dialog", "남해"))
        self.Area_EastChinaSea_Cbox_2.setText(_translate("Dialog", "동중국해"))
        self.label_3.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">&lt; 해달 날짜의 평균 요소 값 &gt;</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "수온"))
        self.label_13.setText(_translate("Dialog", "염분"))
        self.label_14.setText(_translate("Dialog", "용존산소"))
        self.label_18.setText(_translate("Dialog", "인산염인"))
        self.label_16.setText(_translate("Dialog", "아질산질소"))
        self.label_15.setText(_translate("Dialog", "질산질소"))
        self.label_17.setText(_translate("Dialog", "규산규소"))
        self.Page2Button.setText(_translate("Dialog", "          버튼         "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Calender"))
        self.label_26.setText(_translate("Dialog", "수온"))
        self.label_20.setText(_translate("Dialog", "염분"))
        self.label_23.setText(_translate("Dialog", "용존산소"))
        self.PredictPage_3ea_pridet_Button.setText(_translate("Dialog", "확인"))
        self.label_21.setText(_translate("Dialog", "인산염인"))
        self.label_24.setText(_translate("Dialog", "아질산질소"))
        self.label_22.setText(_translate("Dialog", "질산질소"))
        self.label_25.setText(_translate("Dialog", "규산규소"))
        self.PredictPage_4ea_pridet_Button.setText(_translate("Dialog", "확인"))
        self.label_54.setText(_translate("Dialog", "수온"))
        self.label_53.setText(_translate("Dialog", "염분"))
        self.label_59.setText(_translate("Dialog", "인산염인"))
        self.label_55.setText(_translate("Dialog", "용존산소"))
        self.PredictPage_7ea_pridet_Button.setText(_translate("Dialog", "확인"))
        self.label_57.setText(_translate("Dialog", "아질산질소"))
        self.label_56.setText(_translate("Dialog", "질산질소"))
        self.label_58.setText(_translate("Dialog", "규산규소"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Predict"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-family:\'휴먼명조\'; font-size:14pt;\">정선해양관측자료를 통해본 유해적조</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">김준한 · 강민석 · 이동현 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">신라대학교 빅데이터연구실</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\'; font-size:11pt;\">The toxic red tide, ocean observation information through the Choice</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">Kim-Jun Han · Gang-Min Seok · Lee-Dong Hyeon</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">Korea Silla Univercity BigData Lab</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">E-mail : axzswq@sillain.ac.kr</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">적조현상은 우리의 생태계나 인류에게 위협적인 환경문제 중 하나이다. <p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">본 논문에서 저자들은 해양요인들 중 정선해양관측정보에서 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">수온, 염분, 용존산소, 인산염인, 아질산질소, 질산질소, 규산수소의 7개의 요소를 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">python의 pandas 라이브러리를 이용하여서 데이터 추출, 과거적조발생자료를 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">국립수산과학원에서 웹 크롤링한 후에 자료들과 통합하여서 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">영향력을 제공하는 요소를 로지스틱 회귀분석 방식으로 분석했다. </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">2000~2017년 정보들을 대상으로 진행하였다.</span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">본 논문을 통해 해양에 적조가 생기는 이유를 정밀하게 발견하고 </span></p><p align=\"center\"><span style=\" font-family:\'휴먼명조\';\">적조발생을 예방하며 생태계와 학술계에 도움이 되기를 희망한다.</span></p><p align=\"center\"><br/></p><p align=\"center\">담당 교수)윤홍원 교수님</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Epilogue"))


'''
class MainGUI(QtWidgets.QMainWindow,Ui_Dialog)
상속 받은 클래스가 
'''


class MainGUI(QtWidgets.QMainWindow, Ui_Dialog):
    # page2에 필요한 전역 변수
    page2_date = ""  # 날짜
    sea_area = None  # 해역 선택

    my_dict = {"Temperature": ['0'], "Salinity": ['0'], "Dissolved Oxygen": ['0'],
               "Phosphate Phosphorus": ['0'], "Nitrous Acid Nitrogen": ['0'], "Nitric Acid Nitrogen": ['0'],
               "Silicic Acid Silicon": ['0']}


class MainGUI(QtWidgets.QMainWindow, Ui_Dialog):
    my_dict = {"Temperature": ['0'], "Salinity": ['0'], "Dissolved Oxygen": ['0'],
               "Phosphate Phosphorus": ['0'], "Nitrous Acid Nitrogen": ['0'], "Nitric Acid Nitrogen": ['0'],
               "Silicic Acid Silicon": ['0']}
    check_df = pd.DataFrame(my_dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 해당 버튼 클릭 시 해당 함수호출을 선언
        # 1page 버튼
        # 불러오기 버튼
        self.LoadFile_PushButton.clicked.connect(self.get_file_name)
        # '출력하기'버튼
        self.All_Data_read_csv_Pushbutton.clicked.connect(
            lambda state, button=self.All_Data_read_csv_Pushbutton: self.All_Data_ReadClicked(state,
                                                                                              button))  # 1page csv 버튼

        self.Page2Button.clicked.connect(self.Page2PredictpushButton)  # 2page 날짜별 해역별 예측하기 버튼

        # Able lineEdit
        self.WaterTemp_checkBox.stateChanged.connect(lambda: self.WaterTemp_state(self))
        self.Salinity_checkBox.stateChanged.connect(lambda: self.Salinity_state(self))
        self.DissolvedOxygen_checkBox.stateChanged.connect(lambda: self.DissolvedOxygen_state(self))
        self.PhosphatePhosphorus_checkBox.stateChanged.connect(lambda: self.PhosphatePhosphorus_state(self))
        self.NitrousAcidNitrogen_checkBox.stateChanged.connect(lambda: self.NitrousAcidNitrogen_state(self))
        self.NitricAcidNitrogen_checkBox.stateChanged.connect(lambda: self.NitricAcidNitrogen_state(self))
        self.SilicicAcidSilicon_checkBox.stateChanged.connect(lambda: self.SilicicAcidSilicon_state(self))

        # Page2
        self.calendarWidget.clicked.connect(self.__cal_clicked)
        self.Area_EestSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 동해
        self.Area_WestSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 서해
        self.Area_SouthSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 남해
        self.Area_EastChinaSea_Cbox_2.clicked.connect(self.Area_EestSea_state)  # 동중국해

        # Page3
        self.PredictPage_3ea_pridet_Button.clicked.connect(self.Pridict3eaButton)
        self.PredictPage_4ea_pridet_Button.clicked.connect(self.Pridict4eaButton)
        self.PredictPage_7ea_pridet_Button.clicked.connect(self.Pridict7eaButton)

    # 불러오기 기능
    def get_file_name(self):
        filename = QFileDialog.getOpenFileName()
        self.All_Data_read_csv_lineEdit.setText(filename[0])

    def All_Data_ReadClicked(self, state, button):

        # lineEdit에 write한 csv파일을 읽어들임
        # header=0은 해더행 무시한다는 의미. 데이터프레임으로 읽음
        data_frame = pd.read_csv(str(self.All_Data_read_csv_lineEdit.text()), header=0)
        # 종속변수로 선언
        dependent_variable = data_frame['On/Off']

        # 체크된 요소 확인
        print('##############################################################')
        i = 0
        checked_columns = []
        for temp in MainGUI.check_df.iloc[0][:]:
            if temp == 1:
                checked_columns.append(MainGUI.check_df.columns[i])
            i += 1
        print(checked_columns)

        print('##############################################################')

        # 독립변수로 선언
        independent_variables = data_frame[checked_columns]
        # 입력변수에 전체 값이 1인 열을 추가
        independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
        # 로지스틱 회귀모형에 피팅 (NaN행 무시)
        logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

        print('WOW 1')

        # 회귀계수 해석
        def inverse_logit(model_formula):
            from math import exp
            return (1.0 / (1.0 + exp(-model_formula)))

        print(str(logit_model.summary()))

        # 결과창에 출력 (아직 안됌)
        # self.All_Data_read_csv_TextEdit.setText(str(logit_model.summary()))

        ####################################################################### 7.13 여기까지 성공!

        print('0단계')
        # 평균값을 입력시 발생확률
        at_means = float(logit_model.params[0])

        for i in range(0, len(checked_columns)):
            print(checked_columns[i])
            at_means = at_means + float(logit_model.params[i + 1]) * float(data_frame[checked_columns[i]].mean())
        print("첫 for문 통과")
        print("if문 나옴")

        # 7가지 요소들의 평균 값을 입력시 적조발생 확률
        probability = (inverse_logit(at_means)) * 100
        self.All_Data_read_csv_TextEdit.setText(
            str(logit_model.summary()) + "\n" + str(checked_columns) + " 요소들의 평균 값을 입력시 적조 발생 확률 : \n" + str(
                probability) + "%")

    # 체크박스 체크시 LineEdit에 Write 가능하게 만들었습니다.
    # WaterTemp_state라는 함수를 정의
    # setDisable(Ture)는 사용을 못하게 만드는 명령어.
    def WaterTemp_state(self, state):
        if self.WaterTemp_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Temperature'] = 1
        else:
            MainGUI.check_df.ix[0]['Temperature'] = 0

    def Salinity_state(self, state):
        if self.Salinity_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Salinity'] = 1
        else:
            MainGUI.check_df.ix[0]['Salinity'] = 0

    def DissolvedOxygen_state(self, state):
        if self.DissolvedOxygen_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Dissolved Oxygen'] = 1
        else:
            MainGUI.check_df.ix[0]['Dissolved Oxygen'] = 0

    def PhosphatePhosphorus_state(self, state):
        if self.PhosphatePhosphorus_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Phosphate Phosphorus'] = 1
        else:
            MainGUI.check_df.ix[0]['Phosphate Phosphorus'] = 0

    def NitrousAcidNitrogen_state(self, state):
        if self.NitrousAcidNitrogen_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Nitrous Acid Nitrogen'] = 1
        else:
            MainGUI.check_df.ix[0]['Nitrous Acid Nitrogen'] = 0

    def NitricAcidNitrogen_state(self, state):
        if self.NitricAcidNitrogen_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Nitric Acid Nitrogen'] = 1
        else:
            MainGUI.check_df.ix[0]['Nitric Acid Nitrogen'] = 0

    def SilicicAcidSilicon_state(self, state):
        if self.SilicicAcidSilicon_checkBox.isChecked() == True:
            MainGUI.check_df.ix[0]['Silicic Acid Silicon'] = 1
        else:
            MainGUI.check_df.ix[0]['Silicic Acid Silicon'] = 0

    '''
    def onePageSearchpushButton(self):
        #self.textEdit.toPlainText() : GUI에 있는 단어를 가져오는 역할.
        print(self.WaterTempLineEdit.text()) #1page 수온
        print(self.SalinitylineEdit.text()) #1page 염분
        print(self.DissolvedOxygenlineEdit.text())  #1page 용존산소
        print(self.PhosphatePhosphoruslineEdit.text()) #1apge 인산염인
        print(self.NitrousAcidNitrogenlineEdit.text()) #1page 아질산질소
        print(self.NitricAcidNitrogenlineEdit.text()) #1page 질산질소
        print(self.SilicicAcidSiliconlineEdit.text()) #1page 규산규소
    '''

    # 2page에 해역을 선택하는 부분입니다.
    def Area_EestSea_state(self):
        if self.Area_EestSea_Cbox_2.isChecked():
            self.sea_area = "동해"
            print(self.sea_area)
        elif self.Area_WestSea_Cbox_2.isChecked():
            self.sea_area = "서해"
            print(self.sea_area)
        elif self.Area_SouthSea_Cbox_2.isChecked():
            self.sea_area = "남해"
            print(self.sea_area)
        elif self.Area_EastChinaSea_Cbox_2.isChecked():
            self.sea_area = "동중국해"
            print(self.sea_area)

    '''
    def Area_WestSea_state(self, state):


    def Area_SouthSea_state(self, state):


    def Area_EastChinaSea_state(self, state):
    '''

    '''
    Area_EestSea_state
    Area_WestSea_state
    Area_SouthSea_state
    Area_EastChinaSea_state


    self.Area_EestSea_Cbox_2.stateChanged.connect(lambda: self.Area_EestSea_state(self))  # 동해
    self.Area_WestSea_Cbox_2.stateChanged.connect(lambda: self.Area_WestSea_state(self))  # 서해
    self.Area_SouthSea_Cbox_2.stateChanged.connect(lambda: self.Area_SouthSea_state(self))  # 남해
    self.Area_EastChinaSea_Cbox_2.stateChanged.connect(lambda: self.Area_EastChinaSea_state(self))  # 동중국해
    '''

    @pyqtSlot(QDate)
    def __cal_clicked(self, ddate):
        print("-- calendar clicked.....")
        print(ddate.toString())
        tmp_date = str(ddate.toPyDate())
        tmp2 = tmp_date.split("-")
        print(tmp2[0])
        print(tmp2[1])
        print(tmp2[2])
        ddate2 = "".join(tmp2)
        print(tmp_date)
        print(ddate2)
        print("월 = " + str(self.calendarWidget.monthShown()))
        print("년 = " + str(self.calendarWidget.yearShown()))

        self.page2_date = tmp_date  # 전역 클래스의

    def Page2PredictpushButton(self):  # page2의 버튼 누르면 일어나는 현상
        msgbox = QtWidgets.QMessageBox(self)
        tab2_dataframe = pd.read_csv("tab2.csv", header=0, encoding='cp949')
        i_df = pd.DataFrame()

        # 멀티 인덱싱 하여서 groupby 메커니즘 사용
        grouped_ocean_data = tab2_dataframe.groupby(['Sea_area', 'Observation Date'])

        try:
            # 해역 인덱스와 날짜 인덱스의 값이 일치하는 그룹만 불러옵니다.
            i_df = grouped_ocean_data.get_group((self.sea_area, self.page2_date))
            # 위에서 정제된 그룹의 평균을 구합니다.
            i_df = i_df.groupby(['Sea_area', 'Observation Date']).mean()

            # 문자열을 editline이여서 설정형식으로 해주었습니다. 문제는 문자열만 되기에 소수점 3자리 기준으로 문자열 변환
            # 하여서 출력해주었습니다.
            self.theSeasPage_temp_EditLine.setText(str(round(i_df.iloc[0][0], 3)))
            self.theSeasPage_Sal_EditLine.setText(str(round(i_df.iloc[0][1], 3)))
            self.theSeasPage_DisOxy_EditLine.setText(str(round(i_df.iloc[0][2], 3)))
            self.theSeasPage_Phos_EditLine.setText(str(round(i_df.iloc[0][3], 3)))
            self.theSeasPage_Nitrous_EditLine.setText(str(round(i_df.iloc[0][4], 3)))
            self.theSeasPage_Nitric_EditLine.setText(str(round(i_df.iloc[0][5], 3)))
            self.theSeasPage_Sas_EditLine.setText(str(round(i_df.iloc[0][6], 3)))
        except KeyError:  # 912줄에 데이터값이 그룹이 안될경우 이 에러가 뜹니다
            self.Calendar_textEdit.setText("이 날짜에는 데이터가 값이 없습니다.\n 2000~2017년 사이에 지정해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '이 날짜에는 데이터가 값이 없습니다.\n 2000~2017년 사이에 지정해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

            print("이 해역의 이 날짜에는 데이터가 값이 없습니다.")
        except IndexError:  # 문자열 입력 도중에 넣을 데이터 값이 없어서도 안 됩니다.
            self.Calendar_textEdit.setText("이 날짜에는 데이터 값이 없어서 출력도 안 됩니다. \n 2000~2017년 사이에 지정해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '이 날짜에는 데이터 값이 없어서 출력도 안 됩니다.\n 2000~2017년 사이에 지정해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

            print("이 해역의 이 날짜에는 데이터 값이 없어서 출력도 안 됩니다. ㅠㅠ")

    def Pridict3eaButton(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:
            data_frame = pd.read_csv('tab3.csv', header=0)
            dependent_variable = data_frame['On/Off']
            independent_variables = data_frame[['Temperature', 'Salinity', 'Dissolved Oxygen']]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

            input_data1 = float(self.PredictPage_3ea_Temp_Edit.text())
            input_data2 = float(self.PredictPage_3ea_Sal_Edit.text())
            input_data3 = float(self.PredictPage_3ea_DisOxy_Edit.text())

            # 앞 두개의 데이터는 원래의 데이터값을 그대로, 입력받은 값을 배열로 생성
            input_data = np.array([[14.62, 34.19, 5.63], [14.71, 34.19, 5.61],
                                   [input_data1, input_data2, input_data3]])
            df = pd.DataFrame(data=input_data, columns=[independent_variables])

            # 최소 데이터 3개 이상이어야 예측가능
            new_observations = df.ix[data_frame.index.isin(range(3)), independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 4) for score in y_predicted]

            # 예상 확률 출력
            self.PredictPage_3ea_textEdit.setText('적조 발생 확률 : ' + str(round(y_predicted_rounded[2] * 100, 4)) + '%')


        except ValueError:
            self.PredictPage_3ea_textEdit.setText("데이터 값을 입력해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '데이터 값을 입력해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

    def Pridict4eaButton(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:

            data_frame = pd.read_csv('tab3.csv', header=0)
            dependent_variable = data_frame['On/Off']
            independent_variables = data_frame[
                ['Phosphate Phosphorus', 'Nitrous Acid Nitrogen', 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

            input_data1 = float(self.PredictPage_4ea_Phos_Edit.text())
            input_data2 = float(self.PredictPage_4ea_Nitrous_Edit.text())
            input_data3 = float(self.PredictPage_4ea_Nitric_Edit.text())
            input_data4 = float(self.PredictPage_4ea_Sas_Edit.text())

            # 앞 두개의 데이터는 원래의 데이터값을 그대로, 입력받은 값을 배열로 생성
            input_data = np.array([[0.44, 0.68, 7.56, 8.33], [0.41, 0.63, 7.42, 8.13],
                                   [input_data1, input_data2, input_data3, input_data4]])
            df = pd.DataFrame(data=input_data, columns=[independent_variables])

            # 최소 데이터 3개 이상이어야 예측가능
            new_observations = df.ix[data_frame.index.isin(range(3)), independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 4) for score in y_predicted]

            # 예상 확률 출력
            self.PredictPage_4ea_textEdit.setText('적조 발생 확률 : ' + str(round(y_predicted_rounded[2] * 100, 4)) + '%')
        except ValueError:
            self.PredictPage_4ea_textEdit.setText("데이터 값을 입력해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '데이터 값을 입력해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)

    def Pridict7eaButton(self):
        msgbox = QtWidgets.QMessageBox(self)
        try:

            data_frame = pd.read_csv('tab3.csv', header=0)
            dependent_variable = data_frame['On/Off']
            independent_variables = data_frame[
                ['Temperature', 'Salinity', 'Dissolved Oxygen', 'Phosphate Phosphorus', 'Nitrous Acid Nitrogen',
                 'Nitric Acid Nitrogen', 'Silicic Acid Silicon']]
            independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
            logit_model = sm.Logit(dependent_variable, independent_variables_with_constant, missing='drop').fit()

            input_data1 = float(self.PredictPage_7ea_Temp_Edit.text())
            input_data2 = float(self.PredictPage_7ea_Sal_Edit.text())
            input_data3 = float(self.PredictPage_7ea_DisOxy_Edit.text())
            input_data4 = float(self.PredictPage_7ea_Phos_Edit.text())
            input_data5 = float(self.PredictPage_7ea_Nitrous_Edit.text())
            input_data6 = float(self.PredictPage_7ea_Nitric_Edit.text())
            input_data7 = float(self.PredictPage_7ea_Sas_Edit.text())

            # 앞 두개의 데이터는 원래의 데이터값을 그대로, 입력받은 값을 배열로 생성
            input_data = np.array(
                [[14.62, 34.19, 5.63, 0.44, 0.68, 7.56, 8.33], [14.91, 34.21, 5.5, 0.41, 0.63, 7.42, 8.13],
                 [input_data1, input_data2, input_data3, input_data4, input_data5, input_data6, input_data7]])
            df = pd.DataFrame(data=input_data, columns=[independent_variables])

            # 최소 데이터 3개 이상이어야 예측가능
            new_observations = df.ix[data_frame.index.isin(range(3)), independent_variables.columns]
            new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
            y_predicted = logit_model.predict(new_observations_with_constant)
            y_predicted_rounded = [round(score, 4) for score in y_predicted]

            # 예상 확률 출력
            self.PredictPage_7ea_textEdit.setText('적조 발생 확률 : ' + str(round(y_predicted_rounded[2] * 100, 4)) + '%')

        except ValueError:
            self.PredictPage_7ea_textEdit.setText("데이터 값을 입력해주시기 바랍니다.")
            msgbox.question(self, 'No Data', '데이터 값을 입력해주시기 바랍니다.',
                            QtWidgets.QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MainGUI()
    myWindow.show()
    sys.exit(app.exec_())
