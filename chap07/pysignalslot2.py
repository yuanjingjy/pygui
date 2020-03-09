#!/usr/bin/env python
# encoding: utf-8
'''
@Author: yuanjing
@file: pysignalslot2.py
@time: 2020/3/9 13:41
'''

from PyQt5.QtCore import QObject, pyqtSignal
#信号对象
class QTypeSignal(QObject):
    #定义一个信号
    sendmsg = pyqtSignal(str, str)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        self.sendmsg.emit('第一个参数', '第二个参数')


#槽对象
class QTypeslot(QObject):
    def __init__(self):
        super(QTypeslot, self).__init__()

    def get(self,msg1,msg2):
        print("QSlot get msg =>" + msg1 +' ' +msg2)

if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeslot()

    #1
    print("---把信号绑定在槽函数上---")
    send.sendmsg.connect(slot.get)
    send.run()

    #2
    print("把信号从槽函数上解绑")
    send.sendmsg.disconnect(slot.get)
    send.run()

