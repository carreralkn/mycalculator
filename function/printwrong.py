from ui import main_ui
from ui import basic_calculate_ui

from ui import printwrong_ui

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class PrintWrong(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.printwrong_ui = printwrong_ui.Ui_print_wrong()
        self.printwrong_ui.setupUi(self)

        self.printwrong_ui.pushButton_ok.clicked.connect(self.close)
