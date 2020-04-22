from ui import main_ui
from ui import basic_calculate_ui

from function import basic_calculate
from function import more_calculate

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



if __name__ == '__main__':
    # 解决了Qtdesigner设计的界面与实际运行界面不符的问题
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    main = MainWindow()
    basic = basic_calculate.BasicCal()
    more = more_calculate.MoreCal()

    main.show()

    main.main_ui.pushButton_1.clicked.connect(click_1)
    main.main_ui.pushButton_2.clicked.connect(click_2)

    sys.exit(app.exec_())