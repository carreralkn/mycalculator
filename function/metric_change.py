from ui import metric_change_ui

from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MetircCh(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.metric_change_ui = metric_change_ui.Ui_metric_change()
        self.metric_change_ui.setupUi(self)

        self.metric_change_ui.pushButton_l.clicked.connect(self.click_l)
        self.metric_change_ui.pushButton_v.clicked.connect(self.click_v)
        self.metric_change_ui.pushButton_m.clicked.connect(self.click_m)

        # 报错窗口
        self.wrong = printwrong.PrintWrong()

    def click_l(self):
        try:
            text1 = self.metric_change_ui.lineEdit_l1.text()

            # 每个单位到米的转换，即1单位等于多少米

            list_to_m = []
            # 米
            list_to_m.append(1)
            # 毫米
            list_to_m.append(0.001)
            # 厘米
            list_to_m.append(0.01)
            # 分米
            list_to_m.append(0.1)
            # 千米
            list_to_m.append(1000)
            # 寸
            list_to_m.append(500 / 15000)
            # 尺
            list_to_m.append(500 / 1500)
            # 丈
            list_to_m.append(500 / 150)
            # 里
            list_to_m.append(500)
            # 英寸
            list_to_m.append(0.9144 / 36)
            # 英尺
            list_to_m.append(0.9144 / 3)
            # 码
            list_to_m.append(0.9144)
            # 英里
            list_to_m.append(0.9144 * 1760)

            # 取出选中单位的下标
            i1 = self.metric_change_ui.comboBox_l1.currentIndex()
            i2 = self.metric_change_ui.comboBox_l2.currentIndex()

            num1 = eval(text1)

            num = num1 * list_to_m[i1]

            num2 = num / list_to_m[i2]

            text2 = str(round(num2, 5))

            self.metric_change_ui.lineEdit_l2.setText(text2)

        except:
            self.wrong.show()

    def click_v(self):
        try:
            text1 = self.metric_change_ui.lineEdit_v1.text()

            # 每个单位到升的转换，即1单位等于多少升

            list_to_L = []
            # 升
            list_to_L.append(1)
            # 毫升
            list_to_L.append(0.001)
            # 立方米
            list_to_L.append(1000)
            # 品脱
            list_to_L.append(3.7854/8)
            # 夸脱
            list_to_L.append(3.7854/4)
            # 加仑
            list_to_L.append(3.7854)

            # 取出选中单位的下标
            i1 = self.metric_change_ui.comboBox_v1.currentIndex()
            i2 = self.metric_change_ui.comboBox_v2.currentIndex()

            num1 = eval(text1)

            num = num1 * list_to_L[i1]

            num2 = num / list_to_L[i2]

            text2 = str(round(num2, 5))

            self.metric_change_ui.lineEdit_v2.setText(text2)

        except:
            self.wrong.show()

    def click_m(self):
        try:
            text1 = self.metric_change_ui.lineEdit_m1.text()

            # 每个单位到升的转换，即1单位等于多少升

            list_to_g = []
            # 克
            list_to_g.append(1)
            # 毫克
            list_to_g.append(0.001)
            # 千克
            list_to_g.append(1000)
            # 吨
            list_to_g.append(1000000)
            # 磅
            list_to_g.append(453.5924)
            # 盎司
            list_to_g.append(453.5924/16)

            # 取出选中单位的下标
            i1 = self.metric_change_ui.comboBox_m1.currentIndex()
            i2 = self.metric_change_ui.comboBox_m2.currentIndex()

            num1 = eval(text1)

            num = num1 * list_to_g[i1]

            num2 = num / list_to_g[i2]

            text2 = str(round(num2, 5))

            self.metric_change_ui.lineEdit_m2.setText(text2)

        except:
            self.wrong.show()








