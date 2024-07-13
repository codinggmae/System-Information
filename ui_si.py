# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sikvgsgP.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"*{\n"
"border: none;\n"
"}\n"
"QProgressBar{\n"
"background-color: rgb(20, 30, 43);\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"color: rgb(255, 0, 0);\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread: pad, x1:0,y1:0, x2:1, y2:0, stop: 0 rgba(0, 136, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(6, 180, 137);")
        self.header_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setStyleSheet(u"padding: 0;\n"
"margin: 0;")
        self.header_left_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.header_left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.header_left_frame)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"margin: 0;")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/16743131341543238854-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.header_center_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u":/icons/Icons/18175771511543238851-32.png"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignRight)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.header_right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.min_win_btn = QPushButton(self.header_right_frame)
        self.min_win_btn.setObjectName(u"min_win_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/5020973501543238905-128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.min_win_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.min_win_btn)

        self.restore_win_btn = QPushButton(self.header_right_frame)
        self.restore_win_btn.setObjectName(u"restore_win_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/restore-window-line-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_win_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.restore_win_btn)

        self.close_win_btn = QPushButton(self.header_right_frame)
        self.close_win_btn.setObjectName(u"close_win_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/close-line-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_win_btn.setIcon(icon3)
        self.close_win_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_win_btn)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setStyleSheet(u"background-color: rgb(6, 180, 137);")
        self.left_menu_cont_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.pushButton_3 = QPushButton(self.menu_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/6423304151582806558-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_9 = QPushButton(self.menu_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/2458403001543238954-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_9, 6, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_6 = QPushButton(self.menu_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/12637397821543238851-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_8 = QPushButton(self.menu_frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/2010892651596027191-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_8, 5, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_5 = QPushButton(self.menu_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/973587481543238906-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_4 = QPushButton(self.menu_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/12945177681543238861-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.pushButton_7 = QPushButton(self.menu_frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        self.pushButton_7.setFont(font3)
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/66523478616348799344498-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout_3.addWidget(self.cpu_per, 1, 1, 1, 1)

        self.label_15 = QLabel(self.cpu_info_frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_16 = QLabel(self.cpu_info_frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout_3.addWidget(self.cpu_count, 0, 1, 1, 1)

        self.main_core = QLabel(self.cpu_info_frame)
        self.main_core.setObjectName(u"main_core")

        self.gridLayout_3.addWidget(self.main_core, 2, 1, 1, 1)

        self.label_14 = QLabel(self.cpu_info_frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.ram_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_20 = QLabel(self.ram_info_frame)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_4.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_21 = QLabel(self.ram_info_frame)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)

        self.avai_ram = QLabel(self.ram_info_frame)
        self.avai_ram.setObjectName(u"avai_ram")

        self.gridLayout_4.addWidget(self.avai_ram, 1, 1, 1, 1)

        self.label_22 = QLabel(self.ram_info_frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_4.addWidget(self.used_ram, 2, 1, 1, 1)

        self.label_23 = QLabel(self.ram_info_frame)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_4.addWidget(self.free_ram, 3, 1, 1, 1)

        self.label_24 = QLabel(self.ram_info_frame)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 4, 0, 1, 1)

        self.ram_usage = QLabel(self.ram_info_frame)
        self.ram_usage.setObjectName(u"ram_usage")

        self.gridLayout_4.addWidget(self.ram_usage, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_4 = QVBoxLayout(self.battery)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_30 = QLabel(self.battery)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)

        self.verticalLayout_4.addWidget(self.label_30, 0, Qt.AlignmentFlag.AlignBottom)

        self.frame_2 = QFrame(self.battery)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 0, 1, 1)

        self.batt_status = QLabel(self.frame_2)
        self.batt_status.setObjectName(u"batt_status")

        self.gridLayout_5.addWidget(self.batt_status, 0, 1, 1, 1)

        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 1, 0, 1, 1)

        self.charge_status = QLabel(self.frame_2)
        self.charge_status.setObjectName(u"charge_status")

        self.gridLayout_5.addWidget(self.charge_status, 1, 1, 1, 1)

        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_5.addWidget(self.label_33, 2, 0, 1, 1)

        self.batt_time = QLabel(self.frame_2)
        self.batt_time.setObjectName(u"batt_time")

        self.gridLayout_5.addWidget(self.batt_time, 2, 1, 1, 1)

        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_5.addWidget(self.label_34, 3, 0, 1, 1)

        self.plug_status = QLabel(self.frame_2)
        self.plug_status.setObjectName(u"plug_status")

        self.gridLayout_5.addWidget(self.plug_status, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.battery)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_9 = QVBoxLayout(self.sensors)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_55 = QLabel(self.sensors)
        self.label_55.setObjectName(u"label_55")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_55.setFont(font4)

        self.verticalLayout_9.addWidget(self.label_55)

        self.sensor_table = QTableWidget(self.sensors)
        if (self.sensor_table.columnCount() < 6):
            self.sensor_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.sensor_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.sensor_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.sensor_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.sensor_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.sensor_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.sensor_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.sensor_table.setObjectName(u"sensor_table")

        self.verticalLayout_9.addWidget(self.sensor_table)

        self.stackedWidget.addWidget(self.sensors)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_6 = QVBoxLayout(self.activities)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.activities)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_53 = QLabel(self.frame_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_53)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.search_activity_lineEdit = QLineEdit(self.frame_7)
        self.search_activity_lineEdit.setObjectName(u"search_activity_lineEdit")

        self.horizontalLayout_12.addWidget(self.search_activity_lineEdit)

        self.search_activity_btn = QPushButton(self.frame_7)
        self.search_activity_btn.setObjectName(u"search_activity_btn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/9385963701556258272-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_activity_btn.setIcon(icon11)

        self.horizontalLayout_12.addWidget(self.search_activity_btn)


        self.horizontalLayout_11.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.activities)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.activities)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_12 = QPushButton(self.frame_6)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_13.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_6)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_13.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_6)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_13.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_6)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_13.addWidget(self.pushButton_15)


        self.verticalLayout_6.addWidget(self.frame_6, 0, Qt.AlignmentFlag.AlignBottom)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_8 = QVBoxLayout(self.storage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_54 = QLabel(self.storage)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_54)

        self.storage_table = QTableWidget(self.storage)
        if (self.storage_table.columnCount() < 10):
            self.storage_table.setColumnCount(10)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(8, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.storage_table.setHorizontalHeaderItem(9, __qtablewidgetitem23)
        self.storage_table.setObjectName(u"storage_table")

        self.verticalLayout_8.addWidget(self.storage_table)

        self.stackedWidget.addWidget(self.storage)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_5 = QVBoxLayout(self.system_information)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_3 = QFrame(self.system_information)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.system_version = QLabel(self.frame_3)
        self.system_version.setObjectName(u"system_version")

        self.gridLayout_6.addWidget(self.system_version, 3, 1, 1, 1)

        self.system_date = QLabel(self.frame_3)
        self.system_date.setObjectName(u"system_date")

        self.gridLayout_6.addWidget(self.system_date, 4, 1, 1, 1)

        self.system_os = QLabel(self.frame_3)
        self.system_os.setObjectName(u"system_os")
        self.system_os.setFont(font)

        self.gridLayout_6.addWidget(self.system_os, 1, 0, 1, 1)

        self.label_48 = QLabel(self.frame_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)

        self.gridLayout_6.addWidget(self.label_48, 3, 2, 1, 1)

        self.label_49 = QLabel(self.frame_3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.gridLayout_6.addWidget(self.label_49, 4, 2, 1, 1)

        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.gridLayout_6.addWidget(self.label_47, 2, 2, 1, 1)

        self.label_41 = QLabel(self.frame_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_6.addWidget(self.label_41, 2, 0, 1, 1)

        self.system_platform = QLabel(self.frame_3)
        self.system_platform.setObjectName(u"system_platform")

        self.gridLayout_6.addWidget(self.system_platform, 2, 1, 1, 1)

        self.label_43 = QLabel(self.frame_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_6.addWidget(self.label_43, 4, 0, 1, 1)

        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font4)

        self.gridLayout_6.addWidget(self.label_39, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.label_42 = QLabel(self.frame_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font)

        self.gridLayout_6.addWidget(self.label_42, 3, 0, 1, 1)

        self.system_processor = QLabel(self.frame_3)
        self.system_processor.setObjectName(u"system_processor")

        self.gridLayout_6.addWidget(self.system_processor, 2, 3, 1, 1)

        self.system_machine = QLabel(self.frame_3)
        self.system_machine.setObjectName(u"system_machine")

        self.gridLayout_6.addWidget(self.system_machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.frame_3)
        self.system_time.setObjectName(u"system_time")

        self.gridLayout_6.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.networks = QWidget()
        self.networks.setObjectName(u"networks")
        self.verticalLayout_10 = QVBoxLayout(self.networks)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.networks)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 199, 790))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_56 = QLabel(self.frame_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font4)

        self.verticalLayout_12.addWidget(self.label_56)

        self.net_stats_table = QTableWidget(self.frame_8)
        if (self.net_stats_table.columnCount() < 5):
            self.net_stats_table.setColumnCount(5)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_stats_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        self.net_stats_table.setObjectName(u"net_stats_table")
        self.net_stats_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_12.addWidget(self.net_stats_table)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_57 = QLabel(self.frame_9)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_57)

        self.net_io_table = QTableWidget(self.frame_9)
        if (self.net_io_table.columnCount() < 9):
            self.net_io_table.setColumnCount(9)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_io_table.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        self.net_io_table.setObjectName(u"net_io_table")
        self.net_io_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_13.addWidget(self.net_io_table)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_58 = QLabel(self.frame_10)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_58)

        self.net_address_table = QTableWidget(self.frame_10)
        if (self.net_address_table.columnCount() < 6):
            self.net_address_table.setColumnCount(6)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_address_table.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        self.net_address_table.setObjectName(u"net_address_table")
        self.net_address_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_14.addWidget(self.net_address_table)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_59 = QLabel(self.frame_11)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font4)

        self.verticalLayout_15.addWidget(self.label_59)

        self.net_connec_table = QTableWidget(self.frame_11)
        if (self.net_connec_table.columnCount() < 7):
            self.net_connec_table.setColumnCount(7)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.net_connec_table.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        self.net_connec_table.setObjectName(u"net_connec_table")
        self.net_connec_table.setMinimumSize(QSize(0, 150))

        self.verticalLayout_15.addWidget(self.net_connec_table)


        self.verticalLayout_14.addWidget(self.frame_11)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)

        self.right_frame = QFrame(self.main_body_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setStyleSheet(u"background-color: rgb(6, 180, 137);")
        self.right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.right_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame = QFrame(self.right_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/10412341841540553610-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon12)

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_8.addWidget(self.right_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignRight)

        self.size_grip = QFrame(self.footer_right_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.size_grip, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignmentFlag.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"System information", None))
        self.min_win_btn.setText("")
        self.restore_win_btn.setText("")
        self.close_win_btn.setText("")
        self.pushButton_3.setText("")
        self.pushButton_9.setText("")
        self.pushButton_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.pushButton_8.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.pushButton_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u" CPU Count", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Available RAM", None))
        self.avai_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.batt_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.charge_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.batt_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.plug_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem = self.sensor_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem1 = self.sensor_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem2 = self.sensor_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem3 = self.sensor_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem4 = self.sensor_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.search_activity_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.search_activity_btn.setText("")
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem13 = self.storage_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem14 = self.storage_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem15 = self.storage_table.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem16 = self.storage_table.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Max", None));
        ___qtablewidgetitem17 = self.storage_table.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Max File", None));
        ___qtablewidgetitem18 = self.storage_table.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Max Path", None));
        ___qtablewidgetitem19 = self.storage_table.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem20 = self.storage_table.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Free Storage", None));
        ___qtablewidgetitem21 = self.storage_table.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_os.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"System Data", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem22 = self.net_stats_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem23 = self.net_stats_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem24 = self.net_stats_table.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem25 = self.net_stats_table.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem26 = self.net_io_table.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem27 = self.net_io_table.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bytes Sent", None));
        ___qtablewidgetitem28 = self.net_io_table.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Bytes Received", None));
        ___qtablewidgetitem29 = self.net_io_table.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Packets Sent", None));
        ___qtablewidgetitem30 = self.net_io_table.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Packets Received", None));
        ___qtablewidgetitem31 = self.net_io_table.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem32 = self.net_io_table.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem33 = self.net_io_table.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem34 = self.net_io_table.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem35 = self.net_address_table.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem36 = self.net_address_table.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem37 = self.net_address_table.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem38 = self.net_address_table.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem39 = self.net_address_table.horizontalHeaderItem(5)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Network Connections", None))
        ___qtablewidgetitem40 = self.net_connec_table.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem41 = self.net_connec_table.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem42 = self.net_connec_table.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Family", None));
        ___qtablewidgetitem43 = self.net_connec_table.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"LADDR", None));
        ___qtablewidgetitem44 = self.net_connec_table.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem45 = self.net_connec_table.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem46 = self.net_connec_table.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"App Designed and Develoed by Mohammad Mazloom", None))
        self.pushButton_10.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"github", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

