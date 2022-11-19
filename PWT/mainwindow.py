import time
from PySide2.QtCore import *
from PySide2.QtCharts import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from TCPClientwindow import TCPClientWidget
from Rose import Show_Rose
from Heart import Show_Love
Window_IconPath = r"book.png"
TCPClient_Btn_IconPath = r"Switch_btn.png"


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 100)
        self.setWindowTitle("主功能窗口")
        self.setWindowIcon(QIcon(Window_IconPath))  # 需要设置QIcon类型
        self.TCPClientwidget = TCPClientWidget()

        self.TCPClient_Widget_Btn = QPushButton("打开TCPClient窗口", self)
        self.TCPClient_Widget_Btn.clicked.connect(self.TCPClient_Widget_Open)
        self.TCPClient_Widget_Btn.setIcon(QIcon(TCPClient_Btn_IconPath))  # 设置图标
        self.TCPClient_Widget_Btn.setIconSize(QSize(30, 30))  # 设置图标大小

        self.Show_Rose_Btn = QPushButton("显示玫瑰花代码", self)
        self.Show_Rose_Btn.clicked.connect(self.Show_Rose_fun)
        self.Show_Rose_Btn.setIconSize(QSize(30, 30))  # 设置图标大小

        self.Show_Love_Btn = QPushButton("显示爱心代码", self)
        self.Show_Love_Btn.clicked.connect(self.Show_Love_fun)
        self.Show_Love_Btn.setIconSize(QSize(30, 30))  # 设置图标大小

        self.groupBox7 = QGroupBox(self)
        self.verticalLayout10 = QVBoxLayout(self)
        self.verticalLayout10.addWidget(self.TCPClient_Widget_Btn)
        self.verticalLayout10.addWidget(self.Show_Rose_Btn)
        self.verticalLayout10.addWidget(self.Show_Love_Btn)
        self.groupBox7.setLayout(self.verticalLayout10)
        self.herticalLayout12 = QHBoxLayout(self)
        self.herticalLayout12.addWidget(self.groupBox7)
        self.setLayout(self.herticalLayout12)

    @Slot()  # 槽函数标识。窗口切换函数，切换到TCPClient界面。
    def TCPClient_Widget_Open(self):
        # TCPClient_Widget_Btn.setEnabled(False)#按钮状态为待激活。
        self.TCPClientwidget.show()
        self.close()

    @Slot()  # 槽函数标识。窗口切换函数，切换到TCPClient界面。
    def Show_Rose_fun(self):
        Show_Rose()
        self.close()

    @Slot()  # 槽函数标识。窗口切换函数，切换到TCPClient界面。
    def Show_Love_fun(self):
        Show_Love()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwidget = MainWidget()
    mainwidget.show()
    sys.exit(app.exec_())

# def setupUi(self, ChartsWidget):
#     if not ChartsWidget.objectName():
#         ChartsWidget.setObjectName(u"ChartsWidget")
#     ChartsWidget.resize(800, 600)
#     self.verticalLayout = QVBoxLayout(ChartsWidget)
#     self.verticalLayout.setObjectName(u"verticalLayout")
#     self.frameCharts = QFrame(ChartsWidget)
#     self.frameCharts.setObjectName(u"frameCharts")
#     self.frameCharts.setFrameShape(QFrame.StyledPanel)
#     self.frameCharts.setFrameShadow(QFrame.Raised)
#
#     self.verticalLayout.addWidget(self.frameCharts)
#
# self.verticalLayout = QVBoxLayout()

# self.verticalLayout.setObjectName(u"verticalLayout")
# self.frameCharts = QFrame()
#
#     self.x_value = 0
#     self.x_step = 0
#     self.point_cnt = 100
#
#     self.init_charts()
#
#     self.timer = QTimer(self)
#     self.timer.setInterval(100)
#     self.timer.timeout.connect(self.update_charts)
#
#     self.ui.btnStart.setDisabled(False)
#     self.ui.btnStop.setDisabled(True)
#     self.ui.btnStart.clicked.connect(self.start)
#     self.ui.btnStop.clicked.connect(self.stop)
