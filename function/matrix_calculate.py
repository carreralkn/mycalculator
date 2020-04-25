from ui import matrix_calculate_ui

from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import numpy as np
import re

class MatrixCal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.matrix_calculate_ui = matrix_calculate_ui.Ui_matrix_calculate()
        self.matrix_calculate_ui.setupUi(self)

        self.matrix_calculate_ui.pushButton_c.clicked.connect(self.click_c)
        self.matrix_calculate_ui.pushButton_rev.clicked.connect(self.click_rev)
        self.matrix_calculate_ui.pushButton_inv.clicked.connect(self.click_inv)
        self.matrix_calculate_ui.pushButton_det.clicked.connect(self.click_det)
        self.matrix_calculate_ui.pushButton_add.clicked.connect(self.click_add)
        self.matrix_calculate_ui.pushButton_sub.clicked.connect(self.click_sub)
        self.matrix_calculate_ui.pushButton_mul.clicked.connect(self.click_mul)

        # 报错窗口
        self.wrong = printwrong.PrintWrong()

    def click_c(self):
        self.matrix_calculate_ui.textEdit.clear()

    def click_rev(self):
        try:
            text = self.matrix_calculate_ui.textEdit.toPlainText()

            text = text.replace('\n', ';')

            list_matrix = np.mat(text)

            list_matrix = list_matrix.T

            text_new = str(list_matrix)

            # 将字符串矩阵中的中括号[]去除，并使之对齐

            text_new = re.sub('\\[', ' ', text_new)
            text_new = re.sub('\\]', ' ', text_new)

            self.matrix_calculate_ui.textEdit.setText(text_new)

        except:
            self.wrong.show()

    def click_inv(self):
        try:
            text = self.matrix_calculate_ui.textEdit.toPlainText()

            # 用分号替代换行，便于下一步使用np.mat函数
            text = text.replace('\n', ';')

            list_matrix = np.mat(text)

            list_matrix = list_matrix.I

            text_new = str(list_matrix)

            # 将字符串矩阵中的中括号[]去除，并使之对齐

            text_new = re.sub('\\[', ' ', text_new)
            text_new = re.sub('\\]', ' ', text_new)

            self.matrix_calculate_ui.textEdit.setText(text_new)

        except:
            self.wrong.show()

    def click_det(self):
        try:
            text = self.matrix_calculate_ui.textEdit.toPlainText()

            # 用分号替代换行，便于下一步使用np.mat函数
            text = text.replace('\n', ';')

            list_matrix = np.mat(text)

            det = np.linalg.det(list_matrix)

            text_new = str(det)

            self.matrix_calculate_ui.textEdit.setText(text_new)

        except:
            self.wrong.show()

    def click_add(self):
        try:
            text = self.matrix_calculate_ui.textEdit.toPlainText()

            text_list = text.split("\n#\n")

            text_1 = text_list[0]
            text_2 = text_list[1]

            text_1 = text_1.replace('\n', ';')
            text_2 = text_2.replace('\n', ';')

            matrix_1 = np.mat(text_1)
            matrix_2 = np.mat(text_2)

            sum = matrix_1 + matrix_2

            text_new = str(sum)

            # 将字符串矩阵中的中括号[]去除，并使之对齐

            text_new = re.sub('\\[', ' ', text_new)
            text_new = re.sub('\\]', ' ', text_new)

            self.matrix_calculate_ui.textEdit.setText(text_new)

        except:
            self.wrong.show()

    def click_sub(self):
        try:
            text = self.matrix_calculate_ui.textEdit.toPlainText()

            text_list = text.split("\n#\n")

            text_1 = text_list[0]
            text_2 = text_list[1]

            text_1 = text_1.replace('\n', ';')
            text_2 = text_2.replace('\n', ';')

            matrix_1 = np.mat(text_1)
            matrix_2 = np.mat(text_2)

            sum = matrix_1 - matrix_2

            text_new = str(sum)

            # 将字符串矩阵中的中括号[]去除，并使之对齐

            text_new = re.sub('\\[', ' ', text_new)
            text_new = re.sub('\\]', ' ', text_new)

            self.matrix_calculate_ui.textEdit.setText(text_new)

        except:
            self.wrong.show()

    def click_mul(self):
        try:
            text = self.matrix_calculate_ui.textEdit.toPlainText()

            text_list = text.split("\n#\n")

            text_1 = text_list[0]
            text_2 = text_list[1]

            text_1 = text_1.replace('\n', ';')
            text_2 = text_2.replace('\n', ';')

            matrix_1 = np.mat(text_1)
            matrix_2 = np.mat(text_2)

            mul = np.dot(matrix_1,matrix_2)

            text_new = str(mul)

            # 将字符串矩阵中的中括号[]去除，并使之对齐

            text_new = re.sub('\\[', ' ', text_new)
            text_new = re.sub('\\]', ' ', text_new)

            self.matrix_calculate_ui.textEdit.setText(text_new)

        except:
            self.wrong.show()






