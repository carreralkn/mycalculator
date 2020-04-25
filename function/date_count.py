from ui import date_count_ui
from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import datetime

class DateCount(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.date_count_ui = date_count_ui.Ui_date_count()
        self.date_count_ui.setupUi(self)

        self.date_count_ui.calendarWidget.clicked.connect(self.show_date1)
        self.date_count_ui.calendarWidget_2.clicked.connect(self.show_date2)

        self.date_count_ui.pushButton.clicked.connect(self.count)

        # 报错窗口
        self.wrong = printwrong.PrintWrong()

    def count(self):
        date_str1 = self.date_count_ui.lineEdit.text()
        date_str2 = self.date_count_ui.lineEdit_2.text()

        d1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')

        result = d2 - d1
        resultdays = abs(result.days)

        self.date_count_ui.lineEdit_3.setText(str(resultdays))

    def show_date1(self):
        date1 = self.date_count_ui.calendarWidget.selectedDate()
        date_str1 = str(date1.toPyDate())

        self.date_count_ui.lineEdit.setText(date_str1)

    def show_date2(self):
        date2 = self.date_count_ui.calendarWidget_2.selectedDate()
        date_str2 = str(date2.toPyDate())

        self.date_count_ui.lineEdit_2.setText(date_str2)


