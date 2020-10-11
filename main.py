from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.Ui_main import *
import os
import sys
import re, requests
import random
import time

if hasattr(sys, "frozen"):
    os.environ["PATH"] = sys._MEIPASS + ";" + os.environ["PATH"]


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # 获取桌面属性
        self.width = 1920
        self.height = 1040

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        # 开舔
        self.dog.clicked.connect(self.dog_)

        self.resize(888, 555)
        self.move((self.width - 888) / 2, (self.height - 555) / 2)

        self.close_3.clicked.connect(self.ButtonCloseSlot)
        self.max_.clicked.connect(self.ButtonMaxSlot)
        self.min_.clicked.connect(self.ButtonMinSlot)

    def dog_(self):
        url = 'https://we.dog/assets/js/index.js?20200606'
        r = requests.get(url)
        txt = r.text
        titles = re.findall("=\[\'(.*?)\'];", txt)
        # print(titles)
        riji = []
        for i in range(0, len(str(titles).split("\\',\\'"))):
            title = str(titles).split("\\',\\'")[i]
            while str("**") in str(title):
                title = title.replace("**", "")
            # print(title)
            riji.append(title)
        # print("本次舔狗日记共{}条".format(len(riji)))
        tgrj = random.choice(riji)
        date_time = time.strftime('%Y-%m-%d', time.localtime())
        self.text.setText("今天是{}，".format(date_time) + tgrj)

    def ButtonMinSlot(self):
        self.showMinimized()

    def ButtonMaxSlot(self):
        self.resize(888, 555)
        self.move((self.width - 888) / 2, (self.height - 555) / 2)

    def ButtonCloseSlot(self):
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())