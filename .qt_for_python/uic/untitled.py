# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1002, 615)
        font = QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.tabWidget.addTab(self.widget, "")
        self.widget1 = QWidget()
        self.widget1.setObjectName(u"widget1")
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.widget1)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Adobe Song Std")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)
        self.pushButton_4.setMinimumSize(QSize(0, 36))
        self.pushButton_4.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_4, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setMinimumSize(QSize(0, 36))
        self.pushButton_3.setMaximumSize(QSize(200, 50))
        self.pushButton_3.setBaseSize(QSize(0, 0))
        self.pushButton_3.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 36))
        self.pushButton_5.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_5, 5, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 36))
        self.pushButton_6.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Adobe Song Std")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.widget1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMinimumSize(QSize(0, 200))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_8 = QPushButton(self.widget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)
        self.pushButton_8.setMinimumSize(QSize(200, 0))
        self.pushButton_8.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setPointSize(13)
        self.pushButton_8.setFont(font4)

        self.verticalLayout_4.addWidget(self.pushButton_8, 0, Qt.AlignHCenter)

        self.pushButton_7 = QPushButton(self.widget_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(200, 0))
        self.pushButton_7.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(14)
        self.pushButton_7.setFont(font5)

        self.verticalLayout_4.addWidget(self.pushButton_7, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_21 = QWidget(self.tab_2)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_5 = QVBoxLayout(self.widget_21)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit = QTextEdit(self.widget_21)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy5)

        self.verticalLayout_5.addWidget(self.textEdit)


        self.verticalLayout_3.addWidget(self.widget_21)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u57fa\u4e8e\u70b9\u4e91\u6df1\u5ea6\u5b66\u4e60\u7684\u4e09\u7ef4\u7269\u4f53\u6293\u53d6\u4f4d\u59ff\u4f30\u8ba1", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u70b9\u4e91\u6587\u4ef6", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6253\u5f00RGBD\u6587\u4ef6\u5939", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("Form", u"\u52a0\u8f7d\u70b9\u4e91\u6570\u636e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u70b9\u4e91\u964d\u91c7\u6837", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5e73\u9762\u5206\u5272", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5e73\u9762\u5206\u5272", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u63d0\u53d6\u5e73\u9762", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u4f53\u7d20\u964d\u91c7\u6837", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u7edf\u8ba1\u6ee4\u6ce2", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u70b9\u4e91\u6ee4\u6ce2", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8fd9\u662f\u8f93\u51fa\u7684\u547d\u4ee4\u6267\u884c\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget1), QCoreApplication.translate("Form", u"\u70b9\u4e91\u9884\u5904\u7406", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6293\u53d6\u4f4d\u59ff\u4fe1\u606f", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u53ef\u89c6\u5316\u6293\u53d6\u4f4d\u59ff", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fd9\u91cc\u662f\u6253\u5370\u7684\u7ec8\u7aef\u8f93\u51fa.....</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u4f30\u8ba1\u6293\u53d6\u4f4d\u59ff", None))
    # retranslateUi

