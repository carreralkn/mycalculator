from ui import basic_calculate_ui

from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class BasicCal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.basic_calculate_ui = basic_calculate_ui.Ui_basic_calculate()
        self.basic_calculate_ui.setupUi(self)
        self.basic_calculate_ui.pushButton_c.clicked.connect(self.click_c)
        self.basic_calculate_ui.pushButton_0.clicked.connect(self.click_0)
        self.basic_calculate_ui.pushButton_1.clicked.connect(self.click_1)
        self.basic_calculate_ui.pushButton_2.clicked.connect(self.click_2)
        self.basic_calculate_ui.pushButton_3.clicked.connect(self.click_3)
        self.basic_calculate_ui.pushButton_4.clicked.connect(self.click_4)
        self.basic_calculate_ui.pushButton_5.clicked.connect(self.click_5)
        self.basic_calculate_ui.pushButton_6.clicked.connect(self.click_6)
        self.basic_calculate_ui.pushButton_7.clicked.connect(self.click_7)
        self.basic_calculate_ui.pushButton_8.clicked.connect(self.click_8)
        self.basic_calculate_ui.pushButton_9.clicked.connect(self.click_9)
        self.basic_calculate_ui.pushButton_add.clicked.connect(self.click_add)
        self.basic_calculate_ui.pushButton_sub.clicked.connect(self.click_sub)
        self.basic_calculate_ui.pushButton_mul.clicked.connect(self.click_mul)
        self.basic_calculate_ui.pushButton_div.clicked.connect(self.click_div)
        self.basic_calculate_ui.pushButton_point.clicked.connect(self.click_point)

        self.basic_calculate_ui.pushButton_eq.clicked.connect(self.click_eq)

        self.wrong = printwrong.PrintWrong()

    def click_c(self):
        self.basic_calculate_ui.lineEdit.clear()

    def click_0(self):
        self.basic_calculate_ui.lineEdit.insert('0')

    def click_1(self):
        self.basic_calculate_ui.lineEdit.insert('1')

    def click_2(self):
        self.basic_calculate_ui.lineEdit.insert('2')

    def click_3(self):
        self.basic_calculate_ui.lineEdit.insert('3')

    def click_4(self):
        self.basic_calculate_ui.lineEdit.insert('4')

    def click_5(self):
        self.basic_calculate_ui.lineEdit.insert('5')

    def click_6(self):
        self.basic_calculate_ui.lineEdit.insert('6')

    def click_7(self):
        self.basic_calculate_ui.lineEdit.insert('7')

    def click_8(self):
        self.basic_calculate_ui.lineEdit.insert('8')

    def click_9(self):
        self.basic_calculate_ui.lineEdit.insert('9')

    def click_add(self):
        self.basic_calculate_ui.lineEdit.insert('+')

    def click_sub(self):
        self.basic_calculate_ui.lineEdit.insert('-')

    def click_mul(self):
        self.basic_calculate_ui.lineEdit.insert('×')

    def click_div(self):
        self.basic_calculate_ui.lineEdit.insert('÷')

    def click_point(self):
        self.basic_calculate_ui.lineEdit.insert('.')

    def click_eq(self):
        text = self.basic_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(eval(text), 10)
            self.basic_calculate_ui.lineEdit.setText(str(result))
        except:
            self.wrong.show()









