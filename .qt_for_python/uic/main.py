# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog

# 加载PyQt的函数库
from PyQt5 import QtWidgets
from untitled import Ui_Form  # 加载绘制的UI界面
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QInputDialog, QLineEdit # 弹出提示窗
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication    # 二维图片数据显示
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QThread, Qt
import qdarkstyle

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QtWidgets()
#     ui = untitled.Ui_Form()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):  # 系统主界面
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.timer_camera = QTimer(self)
        self.setupUi(self)
        # pixmap = QPixmap("E:\graspnet\graspnet-baseline\doc\example_data\color.png")         # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
        # self.label.setPixmap(pixmap)                                                  # 在label上显示图片
        # self.label.setScaledContents(True)                                            # 让图片自适应label大小
        self.initUI()
        # self.initOpen3d()
        # self.initFuntion()

    def initUI(self):
        # TODO:初始化将所有的界面，全部置为首页显示
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())     # 使用开源插件优化界面

    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()

    sys.exit(app.exec_())