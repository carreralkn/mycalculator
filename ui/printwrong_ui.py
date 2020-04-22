# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printwrong_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_print_wrong(object):
    def setupUi(self, print_wrong):
        print_wrong.setObjectName("print_wrong")
        print_wrong.resize(300, 119)
        self.pushButton_ok = QtWidgets.QPushButton(print_wrong)
        self.pushButton_ok.setGeometry(QtCore.QRect(120, 90, 60, 17))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.label = QtWidgets.QLabel(print_wrong)
        self.label.setGeometry(QtCore.QRect(30, 30, 240, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(print_wrong)
        QtCore.QMetaObject.connectSlotsByName(print_wrong)

    def retranslateUi(self, print_wrong):
        _translate = QtCore.QCoreApplication.translate
        print_wrong.setWindowTitle(_translate("print_wrong", "Wrong"))
        self.pushButton_ok.setText(_translate("print_wrong", "OK"))
        self.label.setText(_translate("print_wrong", "输入数据有误！请重新输入！"))
