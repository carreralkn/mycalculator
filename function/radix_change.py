from ui import radix_change_ui

from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class RadixCh(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.radix_change_ui = radix_change_ui.Ui_radix_change()
        self.radix_change_ui.setupUi(self)

        self.radix_change_ui.pushButton_ce.clicked.connect(self.click_ce)
        self.radix_change_ui.pushButton_0.clicked.connect(self.click_0)
        self.radix_change_ui.pushButton_1.clicked.connect(self.click_1)
        self.radix_change_ui.pushButton_2.clicked.connect(self.click_2)
        self.radix_change_ui.pushButton_3.clicked.connect(self.click_3)
        self.radix_change_ui.pushButton_4.clicked.connect(self.click_4)
        self.radix_change_ui.pushButton_5.clicked.connect(self.click_5)
        self.radix_change_ui.pushButton_6.clicked.connect(self.click_6)
        self.radix_change_ui.pushButton_7.clicked.connect(self.click_7)
        self.radix_change_ui.pushButton_8.clicked.connect(self.click_8)
        self.radix_change_ui.pushButton_9.clicked.connect(self.click_9)
        self.radix_change_ui.pushButton_a.clicked.connect(self.click_a)
        self.radix_change_ui.pushButton_b.clicked.connect(self.click_b)
        self.radix_change_ui.pushButton_c.clicked.connect(self.click_c)
        self.radix_change_ui.pushButton_d.clicked.connect(self.click_d)
        self.radix_change_ui.pushButton_e.clicked.connect(self.click_e)
        self.radix_change_ui.pushButton_f.clicked.connect(self.click_f)

        # 选择输入数据的类型并进行转换
        self.radix_change_ui.pushButton_bin.clicked.connect(self.click_bin)
        self.radix_change_ui.pushButton_oct.clicked.connect(self.click_oct)
        self.radix_change_ui.pushButton_dec.clicked.connect(self.click_dec)
        self.radix_change_ui.pushButton_hex.clicked.connect(self.click_hex)

        # 报错窗口
        self.wrong = printwrong.PrintWrong()

    def click_ce(self):
        self.radix_change_ui.lineEdit.clear()
        self.radix_change_ui.lineEdit_bin.clear()
        self.radix_change_ui.lineEdit_oct.clear()
        self.radix_change_ui.lineEdit_dec.clear()
        self.radix_change_ui.lineEdit_hex.clear()

    def click_0(self):
        self.radix_change_ui.lineEdit.insert('0')

    def click_1(self):
        self.radix_change_ui.lineEdit.insert('1')

    def click_2(self):
        self.radix_change_ui.lineEdit.insert('2')

    def click_3(self):
        self.radix_change_ui.lineEdit.insert('3')

    def click_4(self):
        self.radix_change_ui.lineEdit.insert('4')

    def click_5(self):
        self.radix_change_ui.lineEdit.insert('5')

    def click_6(self):
        self.radix_change_ui.lineEdit.insert('6')

    def click_7(self):
        self.radix_change_ui.lineEdit.insert('7')

    def click_8(self):
        self.radix_change_ui.lineEdit.insert('8')

    def click_9(self):
        self.radix_change_ui.lineEdit.insert('9')

    def click_a(self):
        self.radix_change_ui.lineEdit.insert('A')

    def click_b(self):
        self.radix_change_ui.lineEdit.insert('B')

    def click_c(self):
        self.radix_change_ui.lineEdit.insert('C')

    def click_d(self):
        self.radix_change_ui.lineEdit.insert('D')

    def click_e(self):
        self.radix_change_ui.lineEdit.insert('E')

    def click_f(self):
        self.radix_change_ui.lineEdit.insert('F')

    def click_bin(self):
        text = self.radix_change_ui.lineEdit.text()

        flag = True

        list_bin = ['0', '1']

        for i in text:

            if i not in list_bin:
                flag = False

        if (flag == False):
            self.wrong.show()

        try:
            result = text

            result_bin = bin(int(result,2))
            result_oct = oct(int(result, 2))
            result_dec = int(result, 2)
            result_hex = hex(int(result, 2))

            self.radix_change_ui.lineEdit_bin.setText(str(result_bin))
            self.radix_change_ui.lineEdit_oct.setText(str(result_oct))
            self.radix_change_ui.lineEdit_dec.setText(str(result_dec))
            self.radix_change_ui.lineEdit_hex.setText(str(result_hex))

        except:
            self.wrong.show()

    def click_oct(self):
        text = self.radix_change_ui.lineEdit.text()

        flag = True

        list_oct = ['0', '1', '2', '3', '4', '5', '6', '7']

        for i in text:

            if i not in list_oct:
                flag = False

        if (flag == False):
            self.wrong.show()

        try:
            result = text

            result_bin = bin(int(result, 8))
            result_oct = oct(int(result, 8))
            result_dec = int(result, 8)
            result_hex = hex(int(result, 8))

            self.radix_change_ui.lineEdit_bin.setText(str(result_bin))
            self.radix_change_ui.lineEdit_oct.setText(str(result_oct))
            self.radix_change_ui.lineEdit_dec.setText(str(result_dec))
            self.radix_change_ui.lineEdit_hex.setText(str(result_hex))

        except:
            self.wrong.show()

    def click_dec(self):
        text = self.radix_change_ui.lineEdit.text()

        flag = True

        list_dec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in text:

            if i not in list_dec:
                flag = False

        if (flag == False):
            self.wrong.show()

        try:
            result = text

            result_bin = bin(int(result))
            result_oct = oct(int(result))
            result_dec = int(result)
            result_hex = hex(int(result))

            self.radix_change_ui.lineEdit_bin.setText(str(result_bin))
            self.radix_change_ui.lineEdit_oct.setText(str(result_oct))
            self.radix_change_ui.lineEdit_dec.setText(str(result_dec))
            self.radix_change_ui.lineEdit_hex.setText(str(result_hex))

        except:
            self.wrong.show()

    def click_hex(self):
        text = self.radix_change_ui.lineEdit.text()

        flag = True

        list_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        for i in text:

            if i not in list_hex:
                flag = False

        if (flag == False):
            self.wrong.show()

        try:
            result = text

            result_bin = bin(int(result, 16))
            result_oct = oct(int(result, 16))
            result_dec = int(result, 16)
            result_hex = hex(int(result, 16))

            self.radix_change_ui.lineEdit_bin.setText(str(result_bin))
            self.radix_change_ui.lineEdit_oct.setText(str(result_oct))
            self.radix_change_ui.lineEdit_dec.setText(str(result_dec))
            self.radix_change_ui.lineEdit_hex.setText(str(result_hex))

        except:
            self.wrong.show()

