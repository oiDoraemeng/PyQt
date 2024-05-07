"""
使用打印机
如何将数据输出到打印机
QtPrintSupport
以图像的形式输出
"""
# 创建button,点击button,将button里面的内容输出到打印机

import sys
from PyQt5 import QtGui,QtWidgets,QtPrintSupport
from PyQt5.QtWidgets import *


class PrintSupport(QMainWindow):
    def __init__(self):
        super(PrintSupport, self).__init__()
        # 设置位置
        self.setGeometry(500,200,300,300)

        # 创建button控件
        self.button = QPushButton('打印QTextEdit控件中的内容',self)
        # 设置按钮的位置
        self.button.setGeometry(20,20,260,30)
        # 创建文本控件
        self.editor = QTextEdit('默认文本',self)
        #设置文本控件的位置
        self.editor.setGeometry(20,60,260,200)
        # 绑定信号 槽
        self.button.clicked.connect(self.print)


    # 槽方法
    def print(self):
        # 创建打印对象
        printer = QtPrintSupport.QPrinter()

        # 获得画
        painter = QtGui.QPainter()

        # 把数据绘制到printer里面
        # 将绘制的目标重定向到打印机
        painter.begin(printer)
        # 获得editor屏幕的内容
        screen = self.editor.grab()
        # 设置绘制位置
        painter.drawPixmap(10,10,screen)
        painter.end()
        print("pass")

# 直接运行该脚本，才会执行下面代码
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = PrintSupport()
    gui.show()
    app.exec_()
