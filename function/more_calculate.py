from ui import more_calculate_ui

from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import math

class MoreCal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.more_calculate_ui = more_calculate_ui.Ui_more_calculate()
        self.more_calculate_ui.setupUi(self)

        self.more_calculate_ui.pushButton_c.clicked.connect(self.click_c)
        self.more_calculate_ui.pushButton_0.clicked.connect(self.click_0)
        self.more_calculate_ui.pushButton_1.clicked.connect(self.click_1)
        self.more_calculate_ui.pushButton_2.clicked.connect(self.click_2)
        self.more_calculate_ui.pushButton_3.clicked.connect(self.click_3)
        self.more_calculate_ui.pushButton_4.clicked.connect(self.click_4)
        self.more_calculate_ui.pushButton_5.clicked.connect(self.click_5)
        self.more_calculate_ui.pushButton_6.clicked.connect(self.click_6)
        self.more_calculate_ui.pushButton_7.clicked.connect(self.click_7)
        self.more_calculate_ui.pushButton_8.clicked.connect(self.click_8)
        self.more_calculate_ui.pushButton_9.clicked.connect(self.click_9)
        self.more_calculate_ui.pushButton_pi.clicked.connect(self.click_pi)
        self.more_calculate_ui.pushButton_e.clicked.connect(self.click_e)

        self.more_calculate_ui.pushButton_add.clicked.connect(self.click_add)
        self.more_calculate_ui.pushButton_sub.clicked.connect(self.click_sub)
        self.more_calculate_ui.pushButton_mul.clicked.connect(self.click_mul)
        self.more_calculate_ui.pushButton_div.clicked.connect(self.click_div)
        # 乘幂
        self.more_calculate_ui.pushButton_pow.clicked.connect(self.click_pow)
        self.more_calculate_ui.pushButton_point.clicked.connect(self.click_point)

        self.more_calculate_ui.pushButton_lbr.clicked.connect(self.click_lbr)
        self.more_calculate_ui.pushButton_rbr.clicked.connect(self.click_rbr)

        # 和＝一样为点击直接计算的类型
        self.more_calculate_ui.pushButton_abs.clicked.connect(self.click_abs)
        # 倒数
        self.more_calculate_ui.pushButton_rec.clicked.connect(self.click_rec)
        # 阶乘
        self.more_calculate_ui.pushButton_fac.clicked.connect(self.click_fac)
        self.more_calculate_ui.pushButton_sin.clicked.connect(self.click_sin)
        self.more_calculate_ui.pushButton_cos.clicked.connect(self.click_cos)
        self.more_calculate_ui.pushButton_tan.clicked.connect(self.click_tan)
        self.more_calculate_ui.pushButton_log.clicked.connect(self.click_log)
        self.more_calculate_ui.pushButton_ln.clicked.connect(self.click_ln)

        self.more_calculate_ui.pushButton_eq.clicked.connect(self.click_eq)

        # 报错窗口
        self.wrong = printwrong.PrintWrong()

    def click_c(self):
        self.more_calculate_ui.lineEdit.clear()

    def click_0(self):
        self.more_calculate_ui.lineEdit.insert('0')

    def click_1(self):
        self.more_calculate_ui.lineEdit.insert('1')

    def click_2(self):
        self.more_calculate_ui.lineEdit.insert('2')

    def click_3(self):
        self.more_calculate_ui.lineEdit.insert('3')

    def click_4(self):
        self.more_calculate_ui.lineEdit.insert('4')

    def click_5(self):
        self.more_calculate_ui.lineEdit.insert('5')

    def click_6(self):
        self.more_calculate_ui.lineEdit.insert('6')

    def click_7(self):
        self.more_calculate_ui.lineEdit.insert('7')

    def click_8(self):
        self.more_calculate_ui.lineEdit.insert('8')

    def click_9(self):
        self.more_calculate_ui.lineEdit.insert('9')

    def click_pi(self):
        self.more_calculate_ui.lineEdit.insert(str(round(math.pi, 10)))

    def click_e(self):
        self.more_calculate_ui.lineEdit.insert(str(round(math.e, 10)))

    def click_add(self):
        self.more_calculate_ui.lineEdit.insert('+')

    def click_sub(self):
        self.more_calculate_ui.lineEdit.insert('-')

    def click_mul(self):
        self.more_calculate_ui.lineEdit.insert('×')

    def click_div(self):
        self.more_calculate_ui.lineEdit.insert('÷')

    def click_point(self):
        self.more_calculate_ui.lineEdit.insert('.')

    def click_pow(self):
        self.more_calculate_ui.lineEdit.insert('**')

    def click_lbr(self):
        self.more_calculate_ui.lineEdit.insert('(')

    def click_rbr(self):
        self.more_calculate_ui.lineEdit.insert(')')

    def click_eq(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(eval(text), 10)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()

    def click_abs(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(eval(text), 10)
            result = abs(result)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()

    def click_rec(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(1/eval(text), 10)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()

    def click_fac(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(eval(text), 10)
            flag = True
            result_fac = 1

            if (type(result) != int):
                flag = False

            if (result < 0):
                flag = False
            elif (result == 0):
                result_fac = 1
            else:
                for i in range(1, result+1):
                    result_fac = result_fac * i

            if (flag == True):
                self.more_calculate_ui.lineEdit.setText(str(result_fac))
            else:
                self.wrong.show()

        except:
            self.wrong.show()

    def click_sin(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(math.sin(eval(text)), 10)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()

    def click_cos(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = round(math.cos(eval(text)), 10)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()

    def click_tan(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        flag = True

        x = round(math.pi/2, 10)

        try:
            result = eval(text)
            if (result % x == 0):
                flag = False
            result_tan = math.tan(result)

            if (flag == True):
                result = round(result_tan, 10)
                self.more_calculate_ui.lineEdit.setText(str(result))
            else:
                self.wrong.show()

        except:
            self.wrong.show()

    def click_log(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = eval(text)
            result_log = math.log(result, 10)
            result = round(result_log, 10)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()

    def click_ln(self):
        text = self.more_calculate_ui.lineEdit.text()

        # 将乘号和除号转换为计算机能读取的乘除号
        text = text.replace('×', '*')
        text = text.replace('÷', '/')

        try:
            result = eval(text)
            result_ln = math.log(result, math.e)
            result = round(result_ln, 10)
            self.more_calculate_ui.lineEdit.setText(str(result))

        except:
            self.wrong.show()



