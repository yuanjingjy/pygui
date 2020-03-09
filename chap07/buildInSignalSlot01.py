#!/usr/bin/env python
# encoding: utf-8
'''
@Author: yuanjing
@file: buildInSignalSlot01.py
@time: 2020/3/9 14:05
'''

from PyQt5.QtWidgets import *
import sys

class Winform(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('内置的信号/槽示例')
        self.resize(330,50)
        btn = QPushButton('关闭', self)
        btn.clicked.connect(self.close)

if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())

