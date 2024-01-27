from PyQt5 import QtCore, QtGui, QtWidgets
from customButtons import NotDraggableButton, FlagButton
from mouseoverWidget import MouseoverWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 142)  # 340, 142
        MainWindow.setWindowOpacity(MainWindow.BASE_OPACITY)
        MainWindow.setStyleSheet(f"background-color: rgb({MainWindow.WINDOW_COLOR});")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowIcon(QtGui.QIcon("Icons/main_logo_yellow+blue"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.centralwidget = MouseoverWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.central_Layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.central_Layout.setObjectName("central_Layout")
        self.central_Layout.setContentsMargins(0, 0, 0, 0)

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab")

        print(self.tab1.size(), self.centralwidget.size())

        self.tab1_Layout = QtWidgets.QVBoxLayout(self.tab1)
        self.tab1_Layout.setObjectName("tab1_Layout")

        self.up_frame = QtWidgets.QFrame(self.tab1)
        self.up_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_frame.setObjectName("up_frame")

        self.up_frame_Layout = QtWidgets.QVBoxLayout(self.up_frame)
        self.up_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.up_frame_Layout.setObjectName("up_frame_Layout")

        self.timer_frame = QtWidgets.QFrame(self.up_frame)
        self.timer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timer_frame.setObjectName("timer_frame")

        self.timer_frame_Layout = QtWidgets.QVBoxLayout(self.timer_frame)
        self.timer_frame_Layout.setObjectName("timer_frame_Layout")

        self.timer = QtWidgets.QLabel(self.timer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer.sizePolicy().hasHeightForWidth())
        self.timer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.timer.setFont(font)
        self.timer.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")

        self.timer_frame_Layout.addWidget(self.timer)
        self.up_frame_Layout.addWidget(self.timer_frame, 0, QtCore.Qt.AlignTop)

        self.button_frame = QtWidgets.QFrame(self.up_frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")

        self.button_frame_Layout = QtWidgets.QHBoxLayout(self.button_frame)
        self.button_frame_Layout.setContentsMargins(0, -1, 0, -1)
        self.button_frame_Layout.setObjectName("button_frame_Layout")

        self.close_button = NotDraggableButton(self.button_frame)
        self.close_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setObjectName("close_button")
        self.button_frame_Layout.addWidget(self.close_button)

        self.minimize_button = NotDraggableButton(self.button_frame)
        self.minimize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon1)
        self.minimize_button.setObjectName("minimize_button")
        self.button_frame_Layout.addWidget(self.minimize_button)

        self.pause_button = NotDraggableButton(self.button_frame)
        self.pause_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/play-button-arrowhead.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon2)
        self.pause_button.setObjectName("pause_button")
        self.button_frame_Layout.addWidget(self.pause_button)

        self.flag_button = FlagButton(self.button_frame)
        self.flag_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/pennant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flag_button.setIcon(icon3)
        self.flag_button.setObjectName("flag_button")
        self.button_frame_Layout.addWidget(self.flag_button)

        self.restart_button = NotDraggableButton(self.button_frame)
        self.restart_button.setAcceptDrops(True)
        self.restart_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restart_button.setIcon(icon4)
        self.restart_button.setObjectName("restart_button")
        self.button_frame_Layout.addWidget(self.restart_button)

        self.up_frame_Layout.addWidget(self.button_frame, 0, QtCore.Qt.AlignBottom)
        self.tab1_Layout.addWidget(self.up_frame)

        self.bot_frame = QtWidgets.QFrame(self.tab1)
        self.bot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bot_frame.setObjectName("bot_frame")

        self.bot_frame_Layout = QtWidgets.QVBoxLayout(self.bot_frame)
        self.bot_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.bot_frame_Layout.setObjectName("bot_frame_Layout")

        self.title_frame = QtWidgets.QFrame(self.bot_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")

        self.title_frame_Layout = QtWidgets.QHBoxLayout(self.title_frame)
        self.title_frame_Layout.setContentsMargins(-1, 0, 9, 0)
        self.title_frame_Layout.setObjectName("title_frame_Layout")
        spacerItem = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.title_frame_Layout.addItem(spacerItem)

        self.time_label = QtWidgets.QLabel(self.title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")

        self.title_frame_Layout.addWidget(self.time_label)
        self.all_label = QtWidgets.QLabel(self.title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_label.sizePolicy().hasHeightForWidth())
        self.all_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.all_label.setFont(font)
        self.all_label.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.all_label.setAlignment(QtCore.Qt.AlignCenter)
        self.all_label.setObjectName("all_label")

        self.title_frame_Layout.addWidget(self.all_label)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.title_frame_Layout.addItem(spacerItem1)
        self.bot_frame_Layout.addWidget(self.title_frame)

        self.scroll_frame = QtWidgets.QFrame(self.bot_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_frame.sizePolicy().hasHeightForWidth())
        self.scroll_frame.setSizePolicy(sizePolicy)
        self.scroll_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scroll_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scroll_frame.setObjectName("scroll_frame")

        self.scroll_frame_Layout = QtWidgets.QVBoxLayout(self.scroll_frame)
        self.scroll_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.scroll_frame_Layout.setObjectName("scroll_frame_Layout")

        self.scrollArea = QtWidgets.QScrollArea(self.scroll_frame)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 265, 157))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidget_Layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidget_Layout.setObjectName("scrollAreaWidget_Layout")

        self.scroll_frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.scroll_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scroll_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scroll_frame_2.setObjectName("scroll_frame_2")

        self.scrollArea_Layout = QtWidgets.QHBoxLayout(self.scroll_frame_2)
        self.scrollArea_Layout.setObjectName("scrollArea_Layout")

        self.time_Layout = QtWidgets.QVBoxLayout()
        self.time_Layout.setObjectName("time_Layout")
        self.scrollArea_Layout.addLayout(self.time_Layout)

        self.all_Layout = QtWidgets.QVBoxLayout()
        self.all_Layout.setObjectName("all_Layout")
        self.scrollArea_Layout.addLayout(self.all_Layout)

        self.scrollAreaWidget_Layout.addWidget(self.scroll_frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scroll_frame_Layout.addWidget(self.scrollArea)
        self.bot_frame_Layout.addWidget(self.scroll_frame)
        self.tab1_Layout.addWidget(self.bot_frame)
        self.central_Layout.addWidget(self.tab1)

        # self.tab_2 = QtWidgets.QWidget(self.centralwidget)
        # self.tab_2.setObjectName("tab_2")
        # self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
        # self.verticalLayout_9.setObjectName("verticalLayout_9")
        # self.up_frame_2 = QtWidgets.QFrame(self.tab_2)
        # self.up_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.up_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.up_frame_2.setObjectName("up_frame_2")
        # self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.up_frame_2)
        # self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        # self.verticalLayout_6.setObjectName("verticalLayout_6")
        # self.timer_frame_2 = QtWidgets.QFrame(self.up_frame_2)
        # self.timer_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.timer_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.timer_frame_2.setObjectName("timer_frame_2")
        # self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.timer_frame_2)
        # self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        # spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_6.addItem(spacerItem3)
        # self.timer_2 = QtWidgets.QLabel(self.timer_frame_2)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.timer_2.sizePolicy().hasHeightForWidth())
        # self.timer_2.setSizePolicy(sizePolicy)
        # font = QtGui.QFont()
        # font.setPointSize(32)
        # font.setBold(False)
        # font.setWeight(50)
        # self.timer_2.setFont(font)
        # self.timer_2.setStyleSheet("color: rgb(255, 255, 255);")
        # self.timer_2.setScaledContents(False)
        # self.timer_2.setAlignment(QtCore.Qt.AlignCenter)
        # self.timer_2.setObjectName("timer_2")
        # self.horizontalLayout_6.addWidget(self.timer_2)
        # self.pushButton_2 = NotDraggableButton(self.timer_frame_2)
        # self.pushButton_2.setEnabled(True)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        # self.pushButton_2.setSizePolicy(sizePolicy)
        # self.pushButton_2.setMaximumSize(QtCore.QSize(20, 16777215))
        # self.pushButton_2.setText("")
        # self.pushButton_2.setIcon(icon)
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.horizontalLayout_6.addWidget(self.pushButton_2)
        # self.verticalLayout_6.addWidget(self.timer_frame_2, 0, QtCore.Qt.AlignTop)
        # self.button_frame_2 = QtWidgets.QFrame(self.up_frame_2)
        # self.button_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.button_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.button_frame_2.setObjectName("button_frame_2")
        # self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.button_frame_2)
        # self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        # self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        # self.flag_button_2 = NotDraggableButton(self.button_frame_2)
        # self.flag_button_2.setText("")
        # self.flag_button_2.setIcon(icon1)
        # self.flag_button_2.setObjectName("flag_button_2")
        # self.horizontalLayout_7.addWidget(self.flag_button_2)
        # self.close_button_2 = NotDraggableButton(self.button_frame_2)
        # self.close_button_2.setText("")
        # self.close_button_2.setIcon(icon2)
        # self.close_button_2.setObjectName("close_button_2")
        # self.horizontalLayout_7.addWidget(self.close_button_2)
        # self.minimize_button_2 = NotDraggableButton(self.button_frame_2)
        # self.minimize_button_2.setText("")
        # self.minimize_button_2.setIcon(icon3)
        # self.minimize_button_2.setObjectName("minimize_button_2")
        # self.horizontalLayout_7.addWidget(self.minimize_button_2)
        # self.restart_button_2 = NotDraggableButton(self.button_frame_2)
        # self.restart_button_2.setAcceptDrops(True)
        # self.restart_button_2.setText("")
        # self.restart_button_2.setIcon(icon4)
        # self.restart_button_2.setObjectName("restart_button_2")
        # self.horizontalLayout_7.addWidget(self.restart_button_2)
        # self.verticalLayout_6.addWidget(self.button_frame_2, 0, QtCore.Qt.AlignBottom)
        # self.verticalLayout_9.addWidget(self.up_frame_2)
        # self.bot_frame_2 = QtWidgets.QFrame(self.tab_2)
        # self.bot_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.bot_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.bot_frame_2.setObjectName("bot_frame_2")
        # self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.bot_frame_2)
        # self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        # self.verticalLayout_7.setObjectName("verticalLayout_7")
        # self.timeEdit = QtWidgets.QTimeEdit(self.bot_frame_2)
        # self.timeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        # self.timeEdit.setObjectName("timeEdit")
        # self.verticalLayout_7.addWidget(self.timeEdit)
        # self.verticalLayout_9.addWidget(self.bot_frame_2)

        # self.verticalLayout.addWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        self.timer.setText(_translate("MainWindow", "0:00:00"))
        self.time_label.setText(_translate("MainWindow", "Время"))
        self.all_label.setText(_translate("MainWindow", "Итого"))
        # self.timer_2.setText(_translate("MainWindow", "0:00:00"))
