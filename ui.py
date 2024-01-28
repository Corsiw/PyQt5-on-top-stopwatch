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

        self.tabs = []

        self.tabs.append(QtWidgets.QWidget())
        self.tabs[0].setObjectName("tab")

        self.tabs[0].tab_Layout = QtWidgets.QVBoxLayout(self.tabs[0])
        self.tabs[0].tab_Layout.setObjectName("tab_Layout")

        self.tabs[0].up_frame = QtWidgets.QFrame(self.tabs[0])
        self.tabs[0].up_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].up_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].up_frame.setObjectName("up_frame")

        self.tabs[0].up_frame_Layout = QtWidgets.QVBoxLayout(self.tabs[0].up_frame)
        self.tabs[0].up_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.tabs[0].up_frame_Layout.setObjectName("up_frame_Layout")

        self.tabs[0].timer_frame = QtWidgets.QFrame(self.tabs[0].up_frame)
        self.tabs[0].timer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].timer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].timer_frame.setObjectName("timer_frame")

        self.tabs[0].timer_frame_Layout = QtWidgets.QHBoxLayout(self.tabs[0].timer_frame)
        self.tabs[0].timer_frame_Layout.setObjectName("timer_frame_Layout")
        self.tabs[0].timer_frame_Layout.addStretch(1)

        self.tabs[0].timer = QtWidgets.QLabel(self.tabs[0].timer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs[0].timer.sizePolicy().hasHeightForWidth())
        self.tabs[0].timer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.tabs[0].timer.setFont(font)
        self.tabs[0].timer.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.tabs[0].timer.setAlignment(QtCore.Qt.AlignCenter)
        self.tabs[0].timer.setObjectName("timer")
        self.tabs[0].timer_frame_Layout.addWidget(self.tabs[0].timer, 6)

        self.tabs[0].nextTab_button = NotDraggableButton(self.tabs[0].timer_frame)
        self.tabs[0].nextTab_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[0].nextTab_button.setIcon(icon5)
        self.tabs[0].nextTab_button.setObjectName("nextTub_button")
        self.tabs[0].timer_frame_Layout.addWidget(self.tabs[0].nextTab_button, 0, QtCore.Qt.AlignRight)

        self.tabs[0].up_frame_Layout.addWidget(self.tabs[0].timer_frame, 0, QtCore.Qt.AlignTop)

        self.tabs[0].button_frame = QtWidgets.QFrame(self.tabs[0].up_frame)
        self.tabs[0].button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].button_frame.setObjectName("button_frame")

        self.tabs[0].button_frame_Layout = QtWidgets.QHBoxLayout(self.tabs[0].button_frame)
        self.tabs[0].button_frame_Layout.setContentsMargins(0, -1, 0, -1)
        self.tabs[0].button_frame_Layout.setObjectName("button_frame_Layout")

        self.tabs[0].close_button = NotDraggableButton(self.tabs[0].button_frame)
        self.tabs[0].close_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[0].close_button.setIcon(icon)
        self.tabs[0].close_button.setObjectName("close_button")
        self.tabs[0].button_frame_Layout.addWidget(self.tabs[0].close_button)

        self.tabs[0].minimize_button = NotDraggableButton(self.tabs[0].button_frame)
        self.tabs[0].minimize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[0].minimize_button.setIcon(icon1)
        self.tabs[0].minimize_button.setObjectName("minimize_button")
        self.tabs[0].button_frame_Layout.addWidget(self.tabs[0].minimize_button)

        self.tabs[0].pause_button = NotDraggableButton(self.tabs[0].button_frame)
        self.tabs[0].pause_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/play-button-arrowhead.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[0].pause_button.setIcon(icon2)
        self.tabs[0].pause_button.setObjectName("pause_button")
        self.tabs[0].button_frame_Layout.addWidget(self.tabs[0].pause_button)

        self.tabs[0].flag_button = FlagButton(self.tabs[0].button_frame)
        self.tabs[0].flag_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/pennant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[0].flag_button.setIcon(icon3)
        self.tabs[0].flag_button.setObjectName("flag_button")
        self.tabs[0].button_frame_Layout.addWidget(self.tabs[0].flag_button)

        self.tabs[0].restart_button = NotDraggableButton(self.tabs[0].button_frame)
        self.tabs[0].restart_button.setAcceptDrops(True)
        self.tabs[0].restart_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[0].restart_button.setIcon(icon4)
        self.tabs[0].restart_button.setObjectName("restart_button")
        self.tabs[0].button_frame_Layout.addWidget(self.tabs[0].restart_button)

        self.tabs[0].up_frame_Layout.addWidget(self.tabs[0].button_frame, 0, QtCore.Qt.AlignBottom)
        self.tabs[0].tab_Layout.addWidget(self.tabs[0].up_frame)

        self.tabs[0].bot_frame = QtWidgets.QFrame(self.tabs[0])
        self.tabs[0].bot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].bot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].bot_frame.setObjectName("bot_frame")

        self.tabs[0].bot_frame_Layout = QtWidgets.QVBoxLayout(self.tabs[0].bot_frame)
        self.tabs[0].bot_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.tabs[0].bot_frame_Layout.setObjectName("bot_frame_Layout")

        self.tabs[0].title_frame = QtWidgets.QFrame(self.tabs[0].bot_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs[0].title_frame.sizePolicy().hasHeightForWidth())
        self.tabs[0].title_frame.setSizePolicy(sizePolicy)
        self.tabs[0].title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].title_frame.setObjectName("title_frame")

        self.tabs[0].title_frame_Layout = QtWidgets.QHBoxLayout(self.tabs[0].title_frame)
        self.tabs[0].title_frame_Layout.setContentsMargins(-1, 0, 9, 0)
        self.tabs[0].title_frame_Layout.setObjectName("title_frame_Layout")
        spacerItem = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.tabs[0].title_frame_Layout.addItem(spacerItem)

        self.tabs[0].time_label = QtWidgets.QLabel(self.tabs[0].title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs[0].time_label.sizePolicy().hasHeightForWidth())
        self.tabs[0].time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabs[0].time_label.setFont(font)
        self.tabs[0].time_label.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.tabs[0].time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tabs[0].time_label.setObjectName("time_label")

        self.tabs[0].title_frame_Layout.addWidget(self.tabs[0].time_label)
        self.tabs[0].all_label = QtWidgets.QLabel(self.tabs[0].title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs[0].all_label.sizePolicy().hasHeightForWidth())
        self.tabs[0].all_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabs[0].all_label.setFont(font)
        self.tabs[0].all_label.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.tabs[0].all_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tabs[0].all_label.setObjectName("all_label")

        self.tabs[0].title_frame_Layout.addWidget(self.tabs[0].all_label)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.tabs[0].title_frame_Layout.addItem(spacerItem1)
        self.tabs[0].bot_frame_Layout.addWidget(self.tabs[0].title_frame)

        self.tabs[0].scroll_frame = QtWidgets.QFrame(self.tabs[0].bot_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs[0].scroll_frame.sizePolicy().hasHeightForWidth())
        self.tabs[0].scroll_frame.setSizePolicy(sizePolicy)
        self.tabs[0].scroll_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].scroll_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].scroll_frame.setObjectName("scroll_frame")

        self.tabs[0].scroll_frame_Layout = QtWidgets.QVBoxLayout(self.tabs[0].scroll_frame)
        self.tabs[0].scroll_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.tabs[0].scroll_frame_Layout.setObjectName("scroll_frame_Layout")

        self.tabs[0].scrollArea = QtWidgets.QScrollArea(self.tabs[0].scroll_frame)
        self.tabs[0].scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabs[0].scrollArea.setLineWidth(0)
        self.tabs[0].scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabs[0].scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabs[0].scrollArea.setWidgetResizable(True)
        self.tabs[0].scrollArea.setObjectName("scrollArea")

        self.tabs[0].scrollAreaWidgetContents = QtWidgets.QWidget()
        self.tabs[0].scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 265, 157))
        self.tabs[0].scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tabs[0].scrollAreaWidget_Layout = QtWidgets.QHBoxLayout(self.tabs[0].scrollAreaWidgetContents)
        self.tabs[0].scrollAreaWidget_Layout.setObjectName("scrollAreaWidget_Layout")

        self.tabs[0].scrollArea_frame = QtWidgets.QFrame(self.tabs[0].scrollAreaWidgetContents)
        self.tabs[0].scrollArea_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[0].scrollArea_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[0].scrollArea_frame.setObjectName("scroll_frame")

        self.tabs[0].scrollArea_Layout = QtWidgets.QHBoxLayout(self.tabs[0].scrollArea_frame)
        self.tabs[0].scrollArea_Layout.setObjectName("scrollArea_Layout")

        self.tabs[0].time_Layout = QtWidgets.QVBoxLayout()
        self.tabs[0].time_Layout.setObjectName("time_Layout")
        self.tabs[0].scrollArea_Layout.addLayout(self.tabs[0].time_Layout)

        self.tabs[0].all_Layout = QtWidgets.QVBoxLayout()
        self.tabs[0].all_Layout.setObjectName("all_Layout")
        self.tabs[0].scrollArea_Layout.addLayout(self.tabs[0].all_Layout)

        self.tabs[0].scrollAreaWidget_Layout.addWidget(self.tabs[0].scrollArea_frame)

        self.tabs[0].scrollArea.setWidget(self.tabs[0].scrollAreaWidgetContents)

        self.tabs[0].scroll_frame_Layout.addWidget(self.tabs[0].scrollArea)
        self.tabs[0].bot_frame_Layout.addWidget(self.tabs[0].scroll_frame)
        self.tabs[0].tab_Layout.addWidget(self.tabs[0].bot_frame)
        self.central_Layout.addWidget(self.tabs[0])

        self.tabs.append(QtWidgets.QWidget())
        self.tabs[1].setObjectName("tab")

        self.tabs[1].tab_Layout = QtWidgets.QVBoxLayout(self.tabs[1])
        self.tabs[1].tab_Layout.setObjectName("tab_Layout")

        self.tabs[1].up_frame = QtWidgets.QFrame(self.tabs[1])
        self.tabs[1].up_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[1].up_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[1].up_frame.setObjectName("up_frame")

        self.tabs[1].up_frame_Layout = QtWidgets.QVBoxLayout(self.tabs[1].up_frame)
        self.tabs[1].up_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.tabs[1].up_frame_Layout.setObjectName("up_frame_Layout")

        self.tabs[1].timer_frame = QtWidgets.QFrame(self.tabs[1].up_frame)
        self.tabs[1].timer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[1].timer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[1].timer_frame.setObjectName("timer_frame")

        self.tabs[1].timer_frame_Layout = QtWidgets.QHBoxLayout(self.tabs[1].timer_frame)
        self.tabs[1].timer_frame_Layout.setObjectName("timer_frame_Layout")

        self.tabs[1].prevTab_button = NotDraggableButton(self.tabs[1].timer_frame)
        self.tabs[1].prevTab_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[1].prevTab_button.setIcon(icon6)
        self.tabs[1].prevTab_button.setObjectName("nextTub_button")
        self.tabs[1].timer_frame_Layout.addWidget(self.tabs[1].prevTab_button, 0, QtCore.Qt.AlignLeft)

        self.tabs[1].timer = QtWidgets.QLabel(self.tabs[1].timer_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs[1].timer.sizePolicy().hasHeightForWidth())
        self.tabs[1].timer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.tabs[1].timer.setFont(font)
        self.tabs[1].timer.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        self.tabs[1].timer.setAlignment(QtCore.Qt.AlignCenter)
        self.tabs[1].timer.setObjectName("timer")

        self.tabs[1].timer_frame_Layout.addWidget(self.tabs[1].timer, 6)
        self.tabs[1].timer_frame_Layout.addStretch(1)
        self.tabs[1].up_frame_Layout.addWidget(self.tabs[1].timer_frame, 0, QtCore.Qt.AlignTop)

        self.tabs[1].button_frame = QtWidgets.QFrame(self.tabs[1].up_frame)
        self.tabs[1].button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[1].button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[1].button_frame.setObjectName("button_frame")

        self.tabs[1].button_frame_Layout = QtWidgets.QHBoxLayout(self.tabs[1].button_frame)
        self.tabs[1].button_frame_Layout.setContentsMargins(0, -1, 0, -1)
        self.tabs[1].button_frame_Layout.setObjectName("button_frame_Layout")

        self.tabs[1].close_button = NotDraggableButton(self.tabs[1].button_frame)
        self.tabs[1].close_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[1].close_button.setIcon(icon)
        self.tabs[1].close_button.setObjectName("close_button")
        self.tabs[1].button_frame_Layout.addWidget(self.tabs[1].close_button)

        self.tabs[1].minimize_button = NotDraggableButton(self.tabs[1].button_frame)
        self.tabs[1].minimize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/minimize-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[1].minimize_button.setIcon(icon1)
        self.tabs[1].minimize_button.setObjectName("minimize_button")
        self.tabs[1].button_frame_Layout.addWidget(self.tabs[1].minimize_button)

        self.tabs[1].pause_button = NotDraggableButton(self.tabs[1].button_frame)
        self.tabs[1].pause_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/play-button-arrowhead.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[1].pause_button.setIcon(icon2)
        self.tabs[1].pause_button.setObjectName("pause_button")
        self.tabs[1].button_frame_Layout.addWidget(self.tabs[1].pause_button)

        self.tabs[1].flag_button = FlagButton(self.tabs[1].button_frame)
        self.tabs[1].flag_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/pennant.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[1].flag_button.setIcon(icon3)
        self.tabs[1].flag_button.setObjectName("flag_button")
        self.tabs[1].button_frame_Layout.addWidget(self.tabs[1].flag_button)

        self.tabs[1].restart_button = NotDraggableButton(self.tabs[1].button_frame)
        self.tabs[1].restart_button.setAcceptDrops(True)
        self.tabs[1].restart_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/sync.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabs[1].restart_button.setIcon(icon4)
        self.tabs[1].restart_button.setObjectName("restart_button")
        self.tabs[1].button_frame_Layout.addWidget(self.tabs[1].restart_button)

        self.tabs[1].up_frame_Layout.addWidget(self.tabs[1].button_frame, 0, QtCore.Qt.AlignBottom)
        self.tabs[1].tab_Layout.addWidget(self.tabs[1].up_frame)

        self.tabs[1].bot_frame = QtWidgets.QFrame(self.tabs[1])
        self.tabs[1].bot_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabs[1].bot_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs[1].bot_frame.setObjectName("bot_frame")

        self.tabs[1].bot_frame_Layout = QtWidgets.QVBoxLayout(self.tabs[1].bot_frame)
        self.tabs[1].bot_frame_Layout.setContentsMargins(-1, 0, -1, 0)
        self.tabs[1].bot_frame_Layout.setObjectName("bot_frame_Layout")

        self.tabs[1].tab_Layout.addWidget(self.tabs[1].bot_frame)
        self.central_Layout.addWidget(self.tabs[1])

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        self.tabs[0].timer.setText(_translate("MainWindow", "0:00:00"))
        self.tabs[0].time_label.setText(_translate("MainWindow", "Время"))
        self.tabs[0].all_label.setText(_translate("MainWindow", "Итого"))
        self.tabs[1].timer.setText(_translate("MainWindow", "0:00:00"))
        # self.time_label.setText(_translate("MainWindow", "Время"))
        # self.all_label.setText(_translate("MainWindow", "Итого"))
