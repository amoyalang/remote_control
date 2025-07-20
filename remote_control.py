# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_control.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(848, 469)
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(250, 400, 264, 28))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.max_rota_speed_sb = QDoubleSpinBox(self.layoutWidget_2)
        self.max_rota_speed_sb.setObjectName(u"max_rota_speed_sb")

        self.horizontalLayout_6.addWidget(self.max_rota_speed_sb)

        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 80, 351, 71))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tranlate_c_lb = QLabel(self.widget)
        self.tranlate_c_lb.setObjectName(u"tranlate_c_lb")

        self.horizontalLayout.addWidget(self.tranlate_c_lb)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.rotate_c_lb = QLabel(self.widget)
        self.rotate_c_lb.setObjectName(u"rotate_c_lb")

        self.horizontalLayout.addWidget(self.rotate_c_lb)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(480, 80, 361, 301))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_8 = QLabel(self.widget1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.s0 = QSlider(self.widget1)
        self.s0.setObjectName(u"s0")
        self.s0.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s0)

        self.s1 = QSlider(self.widget1)
        self.s1.setObjectName(u"s1")
        self.s1.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s1)

        self.s2 = QSlider(self.widget1)
        self.s2.setObjectName(u"s2")
        self.s2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s2)

        self.s3 = QSlider(self.widget1)
        self.s3.setObjectName(u"s3")
        self.s3.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s3)

        self.s4 = QSlider(self.widget1)
        self.s4.setObjectName(u"s4")
        self.s4.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s4)

        self.s5 = QSlider(self.widget1)
        self.s5.setObjectName(u"s5")
        self.s5.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s5)

        self.s6 = QSlider(self.widget1)
        self.s6.setObjectName(u"s6")
        self.s6.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.s6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sb_0 = QDoubleSpinBox(self.widget1)
        self.sb_0.setObjectName(u"sb_0")

        self.verticalLayout_5.addWidget(self.sb_0)

        self.sb1 = QDoubleSpinBox(self.widget1)
        self.sb1.setObjectName(u"sb1")

        self.verticalLayout_5.addWidget(self.sb1)

        self.sb2 = QDoubleSpinBox(self.widget1)
        self.sb2.setObjectName(u"sb2")

        self.verticalLayout_5.addWidget(self.sb2)

        self.sb3 = QDoubleSpinBox(self.widget1)
        self.sb3.setObjectName(u"sb3")

        self.verticalLayout_5.addWidget(self.sb3)

        self.sb4 = QDoubleSpinBox(self.widget1)
        self.sb4.setObjectName(u"sb4")

        self.verticalLayout_5.addWidget(self.sb4)

        self.sb5 = QDoubleSpinBox(self.widget1)
        self.sb5.setObjectName(u"sb5")

        self.verticalLayout_5.addWidget(self.sb5)

        self.sb6 = QDoubleSpinBox(self.widget1)
        self.sb6.setObjectName(u"sb6")

        self.verticalLayout_5.addWidget(self.sb6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 150, 468, 232))
        self.horizontalLayout_2 = QHBoxLayout(self.widget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.translate_joy = QWidget(self.widget2)
        self.translate_joy.setObjectName(u"translate_joy")
        self.translate_joy.setMinimumSize(QSize(230, 230))
        self.translate_joy.setMaximumSize(QSize(230, 230))
        self.horizontalLayout_4 = QHBoxLayout(self.translate_joy)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_2.addWidget(self.translate_joy)

        self.rotate_joy = QWidget(self.widget2)
        self.rotate_joy.setObjectName(u"rotate_joy")
        self.rotate_joy.setMinimumSize(QSize(230, 230))
        self.rotate_joy.setMaximumSize(QSize(230, 230))

        self.horizontalLayout_2.addWidget(self.rotate_joy)

        self.widget3 = QWidget(Form)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(20, 400, 201, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.widget3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.max_trans_speed_sb = QDoubleSpinBox(self.widget3)
        self.max_trans_speed_sb.setObjectName(u"max_trans_speed_sb")

        self.horizontalLayout_5.addWidget(self.max_trans_speed_sb)

        self.label_11 = QLabel(self.widget3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5fc3\u4e4b\u7075-RemoteController", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u65cb\u8f6c\u901f\u5ea6:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"rad/s", None))
        self.label.setText(QCoreApplication.translate("Form", u"Robot_Control", None))
        self.tranlate_c_lb.setText(QCoreApplication.translate("Form", u"Translate_Control", None))
        self.rotate_c_lb.setText(QCoreApplication.translate("Form", u"Rotate_Control", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Robotic_Control", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Servo0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Servo1", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Servo2", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Servo3", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Servo4", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Servo5", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u89c6\u89c9\u4e91\u53f0", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6700\u5927\u5e73\u79fb\u901f\u5ea6:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"m/s", None))
    # retranslateUi

