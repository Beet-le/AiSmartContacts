# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1224, 725)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setKerning(False)
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(25, 25, 45, 45))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        # self.label.setStyleSheet("background-color: rgb(10, 46, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(450, 40, 291, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(680, 40, 61, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 40, 81, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 140, 1200, 571))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1198, 569))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1201, 571))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 90, 1191, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout.addWidget(self.pushButton_29)
#         self.pushButton_30 = QtWidgets.QPushButton(Form)
#         self.pushButton_30.setGeometry(QtCore.QRect(1100, 40, 91, 31))
#         self.pushButton_30.setStyleSheet("background-color: rgb(0, 170, 255);\n"
# "color: rgb(255, 255, 255);")
        # self.pushButton_30.setObjectName("pushButton_30")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "AI智能联系人管理"))
        # 设置窗体图标
        # Form.setWindowIcon(QIcon('res/img/ic_launcher.png'))
        self.label_2.setText(_translate("Form", "AI智能联系人管理"))
        self.lineEdit.setPlaceholderText(_translate("Form", "输入搜索内容"))
        self.pushButton.setText(_translate("Form", "搜索"))
        self.pushButton_2.setText(_translate("Form", "添加"))
        self.pushButton_3.setText(_translate("Form", "All"))
        self.pushButton_4.setText(_translate("Form", "A"))
        self.pushButton_6.setText(_translate("Form", "B"))
        self.pushButton_5.setText(_translate("Form", "C"))
        self.pushButton_7.setText(_translate("Form", "D"))
        self.pushButton_8.setText(_translate("Form", "E"))
        self.pushButton_9.setText(_translate("Form", "F"))
        self.pushButton_10.setText(_translate("Form", "G"))
        self.pushButton_11.setText(_translate("Form", "H"))
        self.pushButton_12.setText(_translate("Form", "I"))
        self.pushButton_13.setText(_translate("Form", "J"))
        self.pushButton_14.setText(_translate("Form", "K"))
        self.pushButton_15.setText(_translate("Form", "L"))
        self.pushButton_16.setText(_translate("Form", "M"))
        self.pushButton_17.setText(_translate("Form", "N"))
        self.pushButton_18.setText(_translate("Form", "O"))
        self.pushButton_19.setText(_translate("Form", "P"))
        self.pushButton_20.setText(_translate("Form", "Q"))
        self.pushButton_21.setText(_translate("Form", "R"))
        self.pushButton_22.setText(_translate("Form", "S"))
        self.pushButton_23.setText(_translate("Form", "T"))
        self.pushButton_24.setText(_translate("Form", "U"))
        self.pushButton_25.setText(_translate("Form", "V"))
        self.pushButton_26.setText(_translate("Form", "W"))
        self.pushButton_27.setText(_translate("Form", "X"))
        self.pushButton_28.setText(_translate("Form", "Y"))
        self.pushButton_29.setText(_translate("Form", "Z"))
        # self.pushButton_30.setText(_translate("Form", "查看联系人分布"))
        # 设置要显示的图片
        # self.label.setPixmap(QPixmap('res/img/ic_launcher.png'))
        # 图片显示方式 让图片适应QLabel的大小
        self.label.setScaledContents(True)
