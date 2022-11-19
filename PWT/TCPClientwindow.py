import time
import sys
from PySide2.QtCore import *
from PySide2.QtCharts import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtNetwork import QTcpSocket
from socket import *

sockets = QTcpSocket()


class TCPClientWidget(QWidget):
    def __init__(self, parent=None):
        # global my_TCPClient_size
        super().__init__(parent)
        self.resize(1000, 700)
        self.setWindowTitle("TCPClient通信窗口")

        self.time_label = QLabel(self)
        self.time_label.setMinimumSize(QSize(400, 50))
        self.time_label.setAlignment(Qt.AlignCenter)
        # 创建定时器
        self.Timer = QTimer(self)
        # 定时器每500ms工作一次
        self.Timer.start(500)
        # 建立定时器连接通道  注意这里调用TimeUpdate方法，不是方法返回的的结果，所以不能带括号，写成self.TimeUpdate()是不对的
        self.Timer.timeout.connect(self.TimeUpdate)
        # self.retranslateUi(self)
        # QMetaObject.connectSlotsByName(self)

        self.groupBox1 = QGroupBox(self)
        self.send_text_label = QLabel("发送区", self)
        self.send_data_Text = QTextEdit(self)
        self.TCPClient_clear_send_text_Btn = QPushButton("清空发送区", self)
        self.verticalLayout1 = QVBoxLayout(self)
        self.verticalLayout1.addWidget(self.send_text_label)
        self.verticalLayout1.addWidget(self.send_data_Text)
        self.verticalLayout1.addWidget(self.TCPClient_clear_send_text_Btn)
        self.groupBox1.setLayout(self.verticalLayout1)
        self.herticalLayout1 = QHBoxLayout(self)
        self.herticalLayout1.addWidget(self.groupBox1)
        self.groupBox1.setContentsMargins(0, 0, 0, 0)

        self.groupBox2 = QGroupBox(self)
        self.receive_text_label = QLabel("接收区", self)
        self.receive_data_Text = QTextEdit(self)
        self.TCPClient_clear_receive_text_Btn = QPushButton("清空接收区", self)
        self.verticalLayout3 = QVBoxLayout(self)
        self.verticalLayout3.addWidget(self.receive_text_label)
        self.verticalLayout3.addWidget(self.receive_data_Text)
        self.verticalLayout3.addWidget(self.TCPClient_clear_receive_text_Btn)
        self.groupBox2.setLayout(self.verticalLayout3)
        self.herticalLayout1.addWidget(self.groupBox2)

        self.groupBox4 = QGroupBox(self)
        self.TCPClient_connect_Btn = QPushButton("连接服务器", self)
        self.IP_Address = QLineEdit(self)
        self.port_number = QLineEdit(self)
        self.IP_Address.setText("10.15.178.162")  # 设置提示字
        self.port_number.setText('5000')  # 设置提示字
        self.verticalLayout5 = QVBoxLayout()
        self.verticalLayout5.addWidget(self.time_label)
        self.verticalLayout5.addWidget(self.IP_Address)
        self.verticalLayout5.addWidget(self.port_number)
        self.verticalLayout5.addWidget(self.TCPClient_connect_Btn)
        self.groupBox4.setLayout(self.verticalLayout5)

        self.groupBox5 = QGroupBox(self)
        self.verticalLayout6 = QVBoxLayout(self)
        self.groupBox3 = QGroupBox(self)
        self.send_buff_label = QLabel("发送数据缓冲区", self)
        self.send_data_buff = QTextEdit(self)
        self.TCPClient_send_data_Btn = QPushButton("发送数据", self)
        self.verticalLayout4 = QVBoxLayout(self)
        self.verticalLayout4.addWidget(self.send_buff_label)
        self.verticalLayout4.addWidget(self.send_data_buff)
        self.verticalLayout4.addWidget(self.TCPClient_send_data_Btn)
        self.groupBox3.setLayout(self.verticalLayout4)

        # 设置布局比例
        self.verticalLayout6.addWidget(self.groupBox4)
        # self.verticalLayout6.addStretch(1)
        self.verticalLayout6.addWidget(self.groupBox3)
        # self.verticalLayout6.addStretch(1)

        self.groupBox5.setLayout(self.verticalLayout6)
        self.herticalLayout1.addWidget(self.groupBox5)

        # 布局边界设定
        self.verticalLayout1.setContentsMargins(0, 0, 0, 0)  # 设置上下左右的边距分别为0
        self.verticalLayout5.setContentsMargins(0, 0, 0, 0)  # 设置上下左右的边距分别为0/
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)  # 设置上下左右的边距分别为0
        self.verticalLayout4.setContentsMargins(0, 0, 0, 0)  # 设置上下左右的边距分别为0
        self.verticalLayout6.setContentsMargins(0, 0, 0, 0)  # 设置上下左右的边距分别为0

        self.herticalLayout1.setContentsMargins(0, 0, 0, 0)  # 设置上下左右的边距分别为0

        # 设置控件之间的距离
        self.herticalLayout1.setSpacing(1)
        self.verticalLayout1.setSpacing(1)
        self.verticalLayout3.setSpacing(1)
        self.verticalLayout4.setSpacing(1)
        self.verticalLayout5.setSpacing(1)

        self.setLayout(self.herticalLayout1)

        self.TCPClient_connect_Btn.clicked.connect(self.TCPClient_connect_Btn_Slot)
        self.TCPClient_send_data_Btn.clicked.connect(self.TCPClient_send_data_Btn_Slot)
        self.TCPClient_clear_send_text_Btn.clicked.connect(self.TCPClient_clear_send_text_Btn_Slot)
        self.TCPClient_clear_receive_text_Btn.clicked.connect(self.TCPClient_clear_receive_text_Btn_Slot)

        sockets.connected.connect(self.on_socket_connected)
        sockets.disconnected.connect(self.on_socket_disconnected)
        sockets.readyRead.connect(self.on_socket_receive)

    def TimeUpdate(self):
        # 'yyyy-MM-dd hh:mm:ss dddd' 这是个时间的格式，其中yyyy代表年，MM是月，dd是天，hh是小时，mm是分钟，ss是秒，dddd是星期
        self.time_label.setText(QDateTime.currentDateTime().toString('yyyy年MM月dd日 时间：hh:mm:ss 星期：dddd'))
        if QDateTime.currentDateTime().toString(
                'yyyy年MM月dd日 时间：hh:mm:ss 星期：dddd') == "2022年11月14日 时间：17:06:57 星期：星期一":
            print("s1")
            # 可以设置定时任务

    # def retranslateUi(self):
    #     _translate = QCoreApplication.translate

    def on_socket_receive(self):
        # 接收对方发送过来的数据，最大接收1024个字节
        rxData = str(sockets.readAll())
        self.receive_data_Text.append(rxData)

    def on_socket_connected(self):
        print("连接成功！")
        self.TCPClient_connect_Btn.setEnabled(False)

    def on_socket_disconnected(self):
        print("连接失败！")
        self.TCPClient_connect_Btn.setEnabled(True)

    @Slot()  # 槽函数标识。连接服务器。
    def TCPClient_connect_Btn_Slot(self):
        print("连接服务器按钮已打开")
        server_ip = str(self.IP_Address.text())
        server_port = int(self.port_number.text())
        sockets.connectToHost(server_ip, server_port)

    @Slot()  # 槽函数标识。发送数据。
    def TCPClient_send_data_Btn_Slot(self):
        print("点击了发送数据按钮")
        str1 = self.send_data_buff.toPlainText()  # 接收接收区文本
        sockets.writeData(str1, len(str1))
        self.send_data_Text.append(str1)

    @Slot()  # 槽函数标识。清空发送区。
    def TCPClient_clear_send_text_Btn_Slot(self):
        print("点击了清空发送区按钮")
        self.send_data_Text.clear()

    @Slot()  # 槽函数标识。清空接收区。
    def TCPClient_clear_receive_text_Btn_Slot(self):
        print("点击了清空接收区按钮")
        self.receive_data_Text.clear()

    @Slot()  # 槽函数标识。清空接收区区。
    def TCPClient_receive_data_Slot(self):
        print("接收数据成功")
        # 接收对方发送过来的数据，最大接收1024个字节
        rxData = str(sockets.readAll())
        self.receive_text.append(rxData)

        # self.setWindowIcon(QIcon(IconPath))  # 需要设置QIcon类型
        # TCPClient_Widget_Btn = QPushButton("打开TCPClient窗口", self)
        # TCPClient_Widget_Btn.clicked.connect(self.TCPClient_Widget_Open)


# 调试及代码
def fun():
    app = QApplication(sys.argv)
    mainwidget1 = TCPClientWidget()
    mainwidget1.show()
    sys.exit(app.exec_())
