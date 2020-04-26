# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from picture import background

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(450, 350))
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/newPrefix/background1.jpg);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 10, 300, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪青云W")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 60, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border: 4px double ;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 60, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 4px double ;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 130, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 4px double ;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 130, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"border: 4px double ;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 200, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(150, 150, 227);\n"
"border: 4px double ;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 200, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 142, 76);\n"
"border: 4px double ;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 270, 91, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(170, 170, 100);\n"
"border: 4px double ;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(270, 270, 90, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 151, 151);\n"
"border: 4px double ;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_1.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 18))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我不做计算器了"))
        self.label.setText(_translate("MainWindow", "“我不做计算器了” 科学计算器"))
        self.pushButton_1.setText(_translate("MainWindow", "基础计算"))
        self.pushButton_2.setText(_translate("MainWindow", "拓展计算"))
        self.pushButton_3.setText(_translate("MainWindow", "进制转换"))
        self.pushButton_4.setText(_translate("MainWindow", "矩阵计算"))
        self.pushButton_5.setText(_translate("MainWindow", "度量转换"))
        self.pushButton_6.setText(_translate("MainWindow", "统计功能"))
        self.pushButton_7.setText(_translate("MainWindow", "日期计算"))
        self.pushButton_8.setText(_translate("MainWindow", "退出"))

