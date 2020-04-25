from ui import statistics_ui
from function import printwrong

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import numpy as np
from scipy import stats

class Sta(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.statistics_ui = statistics_ui.Ui_statistics()
        self.statistics_ui.setupUi(self)

        self.statistics_ui.pushButton.clicked.connect(self.click_sta)
        self.statistics_ui.pushButton_c.clicked.connect(self.click_c)

        # 报错窗口
        self.wrong = printwrong.PrintWrong()

    def click_c(self):
        self.statistics_ui.lineEdit.clear()
        self.statistics_ui.lineEdit_2.clear()
        self.statistics_ui.textEdit.clear()
        self.statistics_ui.textEdit_name.clear()

    def click_sta(self):
        try:
            text1 = self.statistics_ui.lineEdit.text()
            text2 = self.statistics_ui.lineEdit_2.text()

            # 第一组数据
            array1 = np.mat(text1)

            array1 = np.array(array1)

            mean1 = np.mean(array1)
            mid1 = np.median(array1)
            mode1 = stats.mode(array1)[0][0][0]
            var1 = np.var(array1)
            std1 = np.std(array1)

            mean2 = 0
            mid2 = 0
            mode2 = 0
            var2 = 0
            std2 = 0
            cov = 0
            cor = 0

            if(text2 != ''):
                # 第二组数据
                array2 = np.mat(text2)

                array2 = np.array(array2)

                mean2 = np.mean(array2)
                mid2 = np.median(array2)
                mode2 = stats.mode(array2)[0][0][0]
                var2 = np.var(array2)
                std2 = np.std(array2)

                # 协方差，取协方差矩阵的第一行第二列的数据，即两组数据的协方差
                cov = np.cov(array1, array2)[0][1]
                # 相关系数，取相关系数矩阵的第一行第二列的数据，即两组数据的相关系数
                cor = np.corrcoef(array1, array2)[0][1]

            if (text2 == ''):
                self.statistics_ui.textEdit.setText(str(mean1))
                self.statistics_ui.textEdit.append(str(mid1))
                self.statistics_ui.textEdit.append(str(mode1))
                self.statistics_ui.textEdit.append(str(var1))
                self.statistics_ui.textEdit.append(str(std1))

                self.statistics_ui.textEdit_name.setText("均值")
                self.statistics_ui.textEdit_name.append("中位数")
                self.statistics_ui.textEdit_name.append("众数")
                self.statistics_ui.textEdit_name.append("方差")
                self.statistics_ui.textEdit_name.append("标准差")

            else:
                self.statistics_ui.textEdit.setText(str(mean1))
                self.statistics_ui.textEdit.append(str(mid1))
                self.statistics_ui.textEdit.append(str(mode1))
                self.statistics_ui.textEdit.append(str(var1))
                self.statistics_ui.textEdit.append(str(std1))
                self.statistics_ui.textEdit.append(str(mean2))
                self.statistics_ui.textEdit.append(str(mid2))
                self.statistics_ui.textEdit.append(str(mode2))
                self.statistics_ui.textEdit.append(str(var2))
                self.statistics_ui.textEdit.append(str(std2))
                self.statistics_ui.textEdit.append(str(cov))
                self.statistics_ui.textEdit.append(str(cor))

                self.statistics_ui.textEdit_name.setText("第一组均值")
                self.statistics_ui.textEdit_name.append("第一组中位数")
                self.statistics_ui.textEdit_name.append("第一组众数")
                self.statistics_ui.textEdit_name.append("第一组方差")
                self.statistics_ui.textEdit_name.append("第一组标差")
                self.statistics_ui.textEdit_name.append("第二组均值")
                self.statistics_ui.textEdit_name.append("第二组中位数")
                self.statistics_ui.textEdit_name.append("第二组众数")
                self.statistics_ui.textEdit_name.append("第二组方差")
                self.statistics_ui.textEdit_name.append("第二组标准差")
                self.statistics_ui.textEdit_name.append("协方差")
                self.statistics_ui.textEdit_name.append("相关系数")

        except:
            self.wrong.show()












