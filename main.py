from ui import main_ui

from function import basic_calculate
from function import more_calculate
from function import radix_change
from function import matrix_calculate
from function import metric_change
from function import statistics
from function import date_count

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = main_ui.Ui_MainWindow()
        self.main_ui.setupUi(self)


def click_1():
    basic.show()


def click_2():
    more.show()


def click_3():
    radix.show()


def click_4():
    matrix.show()


def click_5():
    metric.show()


def click_6():
    sta.show()


def click_7():
    date.show()


def click_8():
    sys.exit(app.exec_())


if __name__ == '__main__':
    # 解决了Qtdesigner设计的界面与实际运行界面不符的问题
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    main = MainWindow()
    basic = basic_calculate.BasicCal()
    more = more_calculate.MoreCal()
    radix = radix_change.RadixCh()
    matrix = matrix_calculate.MatrixCal()
    metric = metric_change.MetircCh()
    sta = statistics.Sta()
    date = date_count.DateCount()

    main.show()

    main.main_ui.pushButton_1.clicked.connect(click_1)
    main.main_ui.pushButton_2.clicked.connect(click_2)
    main.main_ui.pushButton_3.clicked.connect(click_3)
    main.main_ui.pushButton_4.clicked.connect(click_4)
    main.main_ui.pushButton_5.clicked.connect(click_5)
    main.main_ui.pushButton_6.clicked.connect(click_6)
    main.main_ui.pushButton_7.clicked.connect(click_7)
    main.main_ui.pushButton_8.clicked.connect(click_8)

    sys.exit(app.exec_())
