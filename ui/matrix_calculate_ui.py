# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matrix_calculate_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_matrix_calculate(object):
    def setupUi(self, matrix_calculate):
        matrix_calculate.setObjectName("matrix_calculate")
        matrix_calculate.resize(325, 375)
        self.textEdit = QtWidgets.QTextEdit(matrix_calculate)
        self.textEdit.setGeometry(QtCore.QRect(6, 50, 311, 251))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(matrix_calculate)
        self.label.setGeometry(QtCore.QRect(6, 6, 321, 41))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_add = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_add.setGeometry(QtCore.QRect(6, 310, 61, 21))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid ;")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_sub = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_sub.setGeometry(QtCore.QRect(86, 310, 61, 21))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid ;")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_inv = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_inv.setGeometry(QtCore.QRect(6, 341, 61, 21))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_inv.setFont(font)
        self.pushButton_inv.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid ;")
        self.pushButton_inv.setObjectName("pushButton_inv")
        self.pushButton_det = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_det.setGeometry(QtCore.QRect(86, 341, 61, 21))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_det.setFont(font)
        self.pushButton_det.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid ;")
        self.pushButton_det.setObjectName("pushButton_det")
        self.pushButton_rev = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_rev.setGeometry(QtCore.QRect(166, 341, 61, 21))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_rev.setFont(font)
        self.pushButton_rev.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid ;")
        self.pushButton_rev.setObjectName("pushButton_rev")
        self.pushButton_mul = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_mul.setGeometry(QtCore.QRect(166, 310, 61, 21))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(14)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"border: 1px solid ;")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_c = QtWidgets.QPushButton(matrix_calculate)
        self.pushButton_c.setGeometry(QtCore.QRect(246, 310, 71, 51))
        font = QtGui.QFont()
        font.setFamily("汉仪铸字木头人W")
        font.setPointSize(24)
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("background-color: rgb(255, 85, 85);\n"
"border: 4px double ;")
        self.pushButton_c.setObjectName("pushButton_c")
        self.listView = QtWidgets.QListView(matrix_calculate)
        self.listView.setGeometry(QtCore.QRect(0, 0, 331, 381))
        self.listView.setStyleSheet("border-image: url(:/newPrefix/background2.jpg);")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton_add.raise_()
        self.pushButton_sub.raise_()
        self.pushButton_inv.raise_()
        self.pushButton_det.raise_()
        self.pushButton_rev.raise_()
        self.pushButton_mul.raise_()
        self.pushButton_c.raise_()

        self.retranslateUi(matrix_calculate)
        QtCore.QMetaObject.connectSlotsByName(matrix_calculate)

    def retranslateUi(self, matrix_calculate):
        _translate = QtCore.QCoreApplication.translate
        matrix_calculate.setWindowTitle(_translate("matrix_calculate", "矩阵计算"))
        self.textEdit.setHtml(_translate("matrix_calculate", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("matrix_calculate", "请输入矩阵，使用回车键来分隔每一行，使用空格来分隔每一行的元素,使用 # 来分离两个矩阵"))
        self.pushButton_add.setText(_translate("matrix_calculate", "加法"))
        self.pushButton_sub.setText(_translate("matrix_calculate", "减法"))
        self.pushButton_inv.setText(_translate("matrix_calculate", "求逆"))
        self.pushButton_det.setText(_translate("matrix_calculate", "求行列式"))
        self.pushButton_rev.setText(_translate("matrix_calculate", "转置"))
        self.pushButton_mul.setText(_translate("matrix_calculate", "点积"))
        self.pushButton_c.setText(_translate("matrix_calculate", "C"))

