# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date_count_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_date_count(object):
    def setupUi(self, date_count):
        date_count.setObjectName("date_count")
        date_count.resize(410, 400)
        self.label = QtWidgets.QLabel(date_count)
        self.label.setGeometry(QtCore.QRect(20, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(date_count)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 0, 200, 150))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit = QtWidgets.QLineEdit(date_count)
        self.lineEdit.setGeometry(QtCore.QRect(0, 60, 180, 31))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(date_count)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 230, 180, 31))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(date_count)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 120, 30))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(date_count)
        self.calendarWidget_2.setGeometry(QtCore.QRect(180, 170, 200, 150))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.label_3 = QtWidgets.QLabel(date_count)
        self.label_3.setGeometry(QtCore.QRect(20, 340, 120, 30))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(date_count)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 340, 141, 31))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(22)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(date_count)
        self.pushButton.setGeometry(QtCore.QRect(50, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(date_count)
        self.label_4.setGeometry(QtCore.QRect(280, 340, 61, 30))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(date_count)
        QtCore.QMetaObject.connectSlotsByName(date_count)

    def retranslateUi(self, date_count):
        _translate = QtCore.QCoreApplication.translate
        date_count.setWindowTitle(_translate("date_count", "日期计算"))
        self.label.setText(_translate("date_count", "开始时间"))
        self.label_2.setText(_translate("date_count", "结束时间"))
        self.label_3.setText(_translate("date_count", "日期相距"))
        self.pushButton.setText(_translate("date_count", "计算"))
        self.label_4.setText(_translate("date_count", "天"))
