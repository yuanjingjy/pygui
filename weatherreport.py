# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weatherreport.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 381)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 2)
        self.checkbutton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkbutton.setFont(font)
        self.checkbutton.setObjectName("checkbutton")
        self.gridLayout.addWidget(self.checkbutton, 3, 0, 1, 1)
        self.okbutton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.okbutton.setFont(font)
        self.okbutton.setObjectName("okbutton")
        self.gridLayout.addWidget(self.okbutton, 3, 1, 1, 1)
        self.label_2.setBuddy(self.comboBox)

        self.retranslateUi(Form)
        self.checkbutton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "查询城市天气"))
        self.label_2.setText(_translate("Form", "城市"))
        self.comboBox.setItemText(0, _translate("Form", "北京"))
        self.checkbutton.setText(_translate("Form", "查询"))
        self.okbutton.setText(_translate("Form", "确定"))
import apprcc_rc
