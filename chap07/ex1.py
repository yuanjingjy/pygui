#!/usr/bin/env python
# encoding: utf-8
'''
@Author: yuanjing
@file: ex1.py
@time: 2020/3/9 10:48
'''
from PyQt5.QtWidgets import QPushButton, QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
import sys

app = QApplication([])
widget = QWidget()

def showMsg():
    QMessageBox.information(widget,"信息提示框","ok,弹出测试信息")

btn = QPushButton("测试点击按钮", widget)
btn.clicked.connect(showMsg)
widget.show()
sys.exit(app.exec_())

