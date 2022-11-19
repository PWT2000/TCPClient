import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setWindowTitle('QMessageBox例子')
        self.resize(900, 900)

        self.mybutton = QPushButton(self)
        self.mybutton.move(5, 5)
        self.mybutton.setText('点击消息弹出消息框')
        self.reply = QMessageBox
        self.mybutton.clicked.connect(self.msg)



        self.pgb = QProgressBar(self)
        self.pgb.move(500, 500)
        self.pgb.resize(250, 20)
        # 配置一个值表示进度条的当前进度
        self.pv = 0
        # 申明一个时钟控件
        self.timer1 = QBasicTimer()

        # 设置进度条的范围
        self.pgb.setMinimum(0)
        self.pgb.setMaximum(100)
        self.pgb.setValue(self.pv)
        # 载入按钮
        self.btn = QPushButton("开始", self)
        self.btn.move(50, 100)
        self.btn.clicked.connect(self.myTimerState)
        self.show()

    def msg(self):
        # 弹出消息对话框
        reply = QMessageBox.information(self, '标题', '消息对话框正文', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
        if reply == QMessageBox.Yes:  # 判断按钮被点击的状态。
            print("1")
        if reply == QMessageBox.No:  # 判断按钮被点击的状态。
            print("2")

        # self.reply1 = QMessageBox.question(self, "标题", "提问框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # reply2 = QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # reply3 = QMessageBox.critical(self, "标题", "严重错误对话框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # reply4 = QMessageBox.about(self, "标题", "关于对话框消息正文")



    def myTimerState(self):
        if self.timer1.isActive():
            self.timer1.stop()
            self.btn.setText("开始")
        else:
            self.timer1.start(100, self)
            self.btn.setText("停止")

    def timerEvent(self, e):
        if self.pv == 100:
            self.timer1.stop()
            self.btn.setText("完成")
            self.pv = 0
            self.pgb.setValue(self.pv)
        else:
            self.pv += 1
            self.pgb.setValue(self.pv)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
