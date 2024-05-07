import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Factorial(QObject):
    @pyqtSlot(int, result=int)
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.factorial(n-1) * n

class PyFactorial(QWidget):
    def __init__(self):
        super(PyFactorial, self).__init__()
        self.setWindowTitle('Python计算阶乘')
        self.resize(600, 300)
        layout = QVBoxLayout()

        self.browser = QWebEngineView()
        url = os.getcwd() + '/h.html'
        self.browser.load(QUrl.fromLocalFile(url))

        # Initializing QWebChannel
        self.channel = QWebChannel()
        self.factorial_obj = Factorial()
        self.channel.registerObject("obj", self.factorial_obj)
        self.browser.page().setWebChannel(self.channel)

        layout.addWidget(self.browser)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = PyFactorial()
    demo.show()
    sys.exit(app.exec_())
