from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys
import weatherreport
from PyQt5.QtGui import  QIcon,QFont

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.ui = weatherreport.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('读取天气数据')
        self.setWindowIcon(QIcon('Display.ico'))
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setGeometry(200,300,400,400)


if __name__  =='__main__':
    import sys

    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
