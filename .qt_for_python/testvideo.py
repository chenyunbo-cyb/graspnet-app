 
import time
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from cv2 import *
from PyQt5.QtCore import QTimer

class VideoBox(QWidget):

    VIDEO_TYPE_OFFLINE = 0
    VIDEO_TYPE_REAL_TIME = 1

    STATUS_INIT = 0
    STATUS_PLAYING = 1
    STATUS_PAUSE = 2

    video_url = ""

    def __init__(self, video_url="", video_type=VIDEO_TYPE_OFFLINE, auto_play=False):
        QWidget.__init__(self)
        self.video_url = video_url
        self.video_type = video_type  # 0: offline  1: realTime
        self.auto_play = auto_play
        self.status = self.STATUS_INIT  # 0: init 1:playing 2: pause

        # 组件展示
        self.pictureLabel = QLabel()
        # init_image = QPixmap("wzf.jpg").scaled(self.width(), self.height())
        # self.pictureLabel.setPixmap(init_image)

        self.playButton = QPushButton()
        self.playButton.setEnabled(True)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.entry_info)

        control_box = QHBoxLayout()
        control_box.setContentsMargins(0, 0, 0, 0)
        control_box.addWidget(self.playButton)

        layout = QVBoxLayout()
        layout.addWidget(self.pictureLabel)
        layout.addLayout(control_box)

        self.setLayout(layout)

        self.playCapture = VideoCapture(0)
        
    def entry_info(self):
        print('已完成信息录入')
        
        
    def show_video_images(self):
        if self.playCapture.isOpened():
            
            success, frame = self.playCapture.read()
            print('frame.shape:',frame.shape)
            # frame = cvtColor(frame, COLOR_BGR2RGB)
            if success:
                height, width = frame.shape[:2]
                if frame.ndim == 3:
                    rgb = cvtColor(frame, COLOR_BGR2RGB)
                elif frame.ndim == 2:
                    rgb = cvtColor(frame, COLOR_GRAY2BGR)

                temp_image = QImage(rgb.flatten(), width, height, QImage.Format_RGB888)
                temp_pixmap =QPixmap.fromImage(temp_image)
                self.pictureLabel.setPixmap(temp_pixmap)
            else:
                print("read failed, no frame data")
                return
        else:
            print("open file or capturing device error, init again")




if __name__ == "__main__":
    mapp = QApplication(sys.argv)
    mw = VideoBox()

    
    timer = QTimer()
    timer.timeout.connect(mw.show_video_images) #计时结束调用operate()方法
    timer.start(100) #设置计时间隔并启动
    
    mw.show()
    sys.exit(mapp.exec_())