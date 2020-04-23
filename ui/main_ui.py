# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 300, 40))
        font = QtGui.QFont()
        font.setFamily("汉仪青云W")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(100, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 60, 91, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
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
