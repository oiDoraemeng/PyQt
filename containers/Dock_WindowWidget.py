# """
# 停靠控件 (QDockWidget)
#
# 这是一个窗口 可以悬浮 可以拖动
# """
#
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class DockDemo(QMainWindow):
#     def __init__(self,parent=None):
#         super(DockDemo, self).__init__(parent)
#
#         self.setWindowTitle('停靠控件 (QDockWidget)')
#
#         # 水平布局
#         layout = QHBoxLayout()
#         # 创建停靠控件
#         self.items = QDockWidget('Dockable',self)
#         # 创建列表控件
#         self.listWidget = QListWidget()
#         # 为列表控件添加item
#         self.listWidget.addItem('item1')
#         self.listWidget.addItem('item2')
#         self.listWidget.addItem('item3')
#
#         # 将列表控件放到停靠(控件)窗口里面
#         self.items.setWidget(self.listWidget)
#         # 设置中心窗口
#         self.setCentralWidget(QLineEdit())
#         # 添加停靠窗口  在右侧
#         self.addDockWidget(Qt.RightDockWidgetArea,self.items)
#
#         # 默认为停靠状态，可以设置为悬浮
#         self.itms.setFloating(True)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = DockDemo()
#     demo.show()
#     sys.exit(app.exec_())
#
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QDockWidget, QTextEdit, QToolBar, QAction)
from PyQt5.QtCore import Qt
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化UI
        self.initUI()

    def initUI(self):
        # 创建一个QDockWidget
        self.dock = QDockWidget("Dockable", self)
        self.textEdit = QTextEdit()
        self.dock.setWidget(self.textEdit)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # 创建一个工具栏
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)

        # 创建一个动作并添加到工具栏
        toggleDockAction = QAction("Toggle Dock", self)
        toggleDockAction.triggered.connect(self.toggleDockVisibility)
        self.toolbar.addAction(toggleDockAction)

        # 初始化主窗口属性
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Dock Widget Toggle from Toolbar Example')

    def toggleDockVisibility(self):
        # 切换QDockWidget的可见性
        self.dock.setVisible(not self.dock.isVisible())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainApp()
    mainWin.show()
    sys.exit(app.exec_())
