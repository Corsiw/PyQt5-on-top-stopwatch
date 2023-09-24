from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta

from mouseoverWidget import MouseoverWidget
from flagButton import FlagButton
from configuration import Configuration
import os


class TimerWindow(QtWidgets.QMainWindow):
    config = Configuration.getConfig()
    TEXT_COLOR = config["textColor"]
    WINDOW_COLOR = config["windowColor"]
    BASE_OPACITY = config["baseOpacity"]
    NO_FOCUS_OPACITY = config["noFocusOpacity"]
    del config

    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)

        self.timeStarted = None
        self.timePaused = None
        self.isPaused = False

        self.ui.close_btn.clicked.connect(lambda: self.closeBtnEvent())
        self.ui.minimize_btn.clicked.connect(lambda: self.minimizeBtnEvent())
        self.ui.restart_btn.clicked.connect(lambda: self.restartBtnEvent())
        # self.ui.flagbtn.clicked.connect(lambda: self.flagBtnEvent(MainWindow))
        self.ui.pause_btn.clicked.connect(lambda: self.pauseBtnEvent())
        self.s = RestartSignal()
        self.s.restartSignal.connect(self.ui.flag_btn.clearSliderWidget)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(50)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # def eventFilter(self, source, event):
    #     if source == self.centralWidget:
    #         if event.type() == QtCore.QEvent.MouseButtonPress:
    #             self.offset = event.pos()
    #         elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
    #             # no need for complex computations: just use the offset to compute
    #             # "delta" position, and add that to the current one
    #             self.move(self.pos() - self.offset + event.pos())
    #             # return True to tell Qt that the event has been accepted and
    #             # should not be processed any further
    #             return True
    #         elif event.type() == QtCore.QEvent.MouseButtonRelease:
    #             self.offset = None
    #     # let Qt process any other event
    #     return super().eventFilter(source, event)
    def closeBtnEvent(self):
        self.close()

    def minimizeBtnEvent(self):
        self.showMinimized()

    def pauseBtnEvent(self):
        if self.isPaused:
            pauseTime = datetime.now() - self.timePaused
            self.timeStarted = self.timeStarted + pauseTime
            self.isPaused = False
            self.ui.pause_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\pause.png'))

        elif self.timeStarted:
            self.timePaused = datetime.now()
            self.isPaused = True
            self.ui.pause_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\play-button-arrowhead.png'))

        else:
            self.timeStarted = datetime.now()
            self.ui.pause_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\pause.png'))

    def restartBtnEvent(self):

        self.s.restartSignal.emit()
        self.timeStarted = None
        self.timePaused = None
        self.isPaused = False

        self.ui.pause_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\play-button-arrowhead.png'))

    def showTime(self):
        if self.isPaused is False:
            if self.timeStarted is None:
                self.ui.timer_label.setText(str(timedelta()))
            else:
                t = str(datetime.now() - self.timeStarted)
                t = t[:t.find(".") + 3]
                self.ui.timer_label.setText(t)


class RestartSignal(QtWidgets.QWidget):
    restartSignal = QtCore.pyqtSignal()


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Timer")
        MainWindow.setWindowTitle("Timer")
        MainWindow.resize(340, 160)
        MainWindow.setWindowOpacity(0.7)
        MainWindow.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.centralwidget = MouseoverWidget(MainWindow)
        self.centralwidget.setStyleSheet(f"background-color: rgb({MainWindow.WINDOW_COLOR});")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.installEventFilter(MainWindow)
        self.centralwidget.acceptDrops()

        # deltaTimeLabel
        self.deltaTimeLabel = QtWidgets.QLabel("Время", self.centralwidget)
        self.deltaTimeLabel.setGeometry(QtCore.QRect(55, 157, 60, 20))
        self.deltaTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deltaTimeLabel.setFont(font)
        self.deltaTimeLabel.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        # allTimeLabel
        self.allTimeLabel = QtWidgets.QLabel("Итого", self.centralwidget)
        self.allTimeLabel.setGeometry(QtCore.QRect(210, 157, 60, 20))
        self.allTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.allTimeLabel.setFont(font)
        self.allTimeLabel.setStyleSheet(f"color: rgb({MainWindow.TEXT_COLOR});")
        # scroll
        self.scroll = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll.setObjectName("scroll")
        self.scroll.setGeometry(QtCore.QRect(0, 180, 340, 140))
        self.scroll.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.scrollwidget = QtWidgets.QWidget(self.scroll)
        self.scrollwidget.setObjectName("scrollwidget")

        self.deltaTimeWidget = QtWidgets.QWidget(self.scrollwidget)
        self.deltaTimeWidget.setObjectName("deltaTimeWidget")
        self.allTimeWidget = QtWidgets.QWidget(self.scrollwidget)
        self.allTimeWidget.setObjectName("allTimeWidget")

        self.box = QtWidgets.QHBoxLayout()
        self.deltaTimeVBox, self.allTimeVBox = QtWidgets.QVBoxLayout(), QtWidgets.QVBoxLayout()

        self.deltaTimeWidget.setLayout(self.deltaTimeVBox)
        self.allTimeWidget.setLayout(self.allTimeVBox)

        self.box.addWidget(self.deltaTimeWidget)
        self.box.addWidget(self.allTimeWidget)

        self.scrollwidget.setLayout(self.box)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.scrollwidget)
        # close_btn
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(10, 110, 40, 40))
        self.close_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.close_btn.setObjectName("close_btn")
        self.close_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\close.png'))
        # minimize_btn
        self.minimize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.minimize_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.minimize_btn.setObjectName("minimize_btn")
        self.minimize_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\minimize-sign.png'))
        # pause_btn
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.pause_btn.setObjectName("pause_btn")
        self.pause_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\play-button-arrowhead.png'))
        # flag_btn
        self.flag_btn = FlagButton(self.centralwidget)
        self.flag_btn.setEnabled(True)
        self.flag_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.flag_btn.setObjectName("flag_btn")
        self.flag_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\pennant.png'))
        # restart_btn
        self.restart_btn = QtWidgets.QPushButton(self.centralwidget)
        self.restart_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.restart_btn.setObjectName("restart_btn")
        self.restart_btn.setIcon(QtGui.QIcon(os.getcwd() + '\Icons\sync.png'))
        # buttons_tab
        self.buttonsHLayout = QtWidgets.QHBoxLayout()
        self.buttonsHLayout.addWidget(self.close_btn)
        self.buttonsHLayout.addWidget(self.minimize_btn)
        self.buttonsHLayout.addWidget(self.pause_btn)
        self.buttonsHLayout.addWidget(self.flag_btn)
        self.buttonsHLayout.addWidget(self.restart_btn)
        self.buttonsTab = QtWidgets.QWidget(self.centralwidget)
        self.buttonsTab.setGeometry(QtCore.QRect(0, 110, 340, 40))
        self.buttonsTab.setLayout(self.buttonsHLayout)
        # timer
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(10, 10, 320, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.timer_label.setFont(font)
        self.timer_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timer_label.setStyleSheet(f"color: rgb({TimerWindow.TEXT_COLOR});")
        self.timer_label.setTextFormat(QtCore.Qt.AutoText)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.timer_label.setWordWrap(False)
        self.timer_label.setObjectName("timer_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + '\Icons\main_logo_yellow+blue.png'))
        self.timer_label.setText(_translate("MainWindow", "0:00:00"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TimerWindow()
    MainWindow.show()
    sys.exit(app.exec_())
