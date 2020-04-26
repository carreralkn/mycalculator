# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statistics(object):
    def setupUi(self, statistics):
        statistics.setObjectName("statistics")
        statistics.resize(400, 300)
        self.label = QtWidgets.QLabel(statistics)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 30))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(statistics)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 400, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(statistics)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 400, 30))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(statistics)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 90, 400, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(statistics)
        self.pushButton.setGeometry(QtCore.QRect(120, 125, 60, 20))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"border: 1px solid ;")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(statistics)
        self.textEdit.setGeometry(QtCore.QRect(110, 150, 290, 140))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_c = QtWidgets.QPushButton(statistics)
        self.pushButton_c.setGeometry(QtCore.QRect(240, 125, 60, 20))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("background-color: rgb(255, 85, 85);\n"
"border: 1px solid ;")
        self.pushButton_c.setObjectName("pushButton_c")
        self.textEdit_name = QtWidgets.QTextEdit(statistics)
        self.textEdit_name.setGeometry(QtCore.QRect(0, 150, 111, 140))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.textEdit_name.setFont(font)
        self.textEdit_name.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.textEdit_name.setReadOnly(True)
        self.textEdit_name.setObjectName("textEdit_name")
        self.listWidget = QtWidgets.QListWidget(statistics)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.listWidget.setStyleSheet("border-image: url(:/newPrefix/background2.jpg);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.textEdit.raise_()
        self.pushButton_c.raise_()
        self.textEdit_name.raise_()

        self.retranslateUi(statistics)
        QtCore.QMetaObject.connectSlotsByName(statistics)

    def retranslateUi(self, statistics):
        _translate = QtCore.QCoreApplication.translate
        statistics.setWindowTitle(_translate("statistics", "统计功能"))
        self.label.setText(_translate("statistics", "输入一组数据，每个数据用空格隔开"))
        self.label_2.setText(_translate("statistics", "输入第二组数据（可选），若输入则统计两组数据的协方差与相关系数"))
        self.pushButton.setText(_translate("statistics", "统计"))
        self.textEdit.setHtml(_translate("statistics", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.pushButton_c.setText(_translate("statistics", "C"))
