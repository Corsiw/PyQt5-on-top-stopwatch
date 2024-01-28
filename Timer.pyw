from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta

from ui import Ui_MainWindow
from configuration import Configuration
from os import getcwd


class TimerWindow(QtWidgets.QMainWindow):
    config = Configuration.getConfig()
    TEXT_COLOR = config["textColor"]
    WINDOW_COLOR = config["windowColor"]
    BASE_OPACITY = config["baseOpacity"]
    NO_FOCUS_OPACITY = config["noFocusOpacity"]
    del config

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        for tab in self.ui.tabs:
            tab.hide()
        self.curTab = 0
        self.ui.tabs[self.curTab].show()

        self.ui.tabs[self.curTab].bot_frame.hide()
        self.isBotFrameShown = False
        self.setMinimumSize(340, 92)
        self.resize(340, 142)
        self.prevSize = self.size()
        self.oldPos = None
        self.draggable = True
        self.ui.centralwidget.mouseoverEvent.connect(lambda event: self.mouseoverEvent(event))

        self.ui.tabs[0].nextTab_button.clicked.connect(lambda: self.nextTabBtnEvent())

        self.ui.tabs[0].close_button.clicked.connect(lambda: self.closeBtnEvent())
        self.ui.tabs[0].close_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.tabs[1].close_button.clicked.connect(lambda: self.closeBtnEvent())
        self.ui.tabs[1].close_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.tabs[0].minimize_button.clicked.connect(lambda: self.minimizeBtnEvent())
        self.ui.tabs[0].minimize_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.tabs[1].minimize_button.clicked.connect(lambda: self.minimizeBtnEvent())
        self.ui.tabs[1].minimize_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.tabs[0].pause_button.clicked.connect(lambda: self.pauseBtnEvent(self.ui.tabs[0].pause_button))
        self.ui.tabs[0].pause_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.tabs[1].pause_button.clicked.connect(lambda: self.pauseBtnEvent(self.ui.tabs[1].pause_button))
        self.ui.tabs[1].pause_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.lastFlag = None
        self.ui.tabs[0].flag_button.clickSignal.connect(self.flagClickedSlot)
        self.ui.tabs[0].flag_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.tabs[1].flag_button.clickSignal.connect(self.flagClickedSlot)
        self.ui.tabs[1].flag_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.tabs[0].restart_button.clicked.connect(lambda: self.restartBtnEvent())
        self.ui.tabs[0].restart_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.tabs[1].restart_button.clicked.connect(lambda: self.restartBtnEvent())
        self.ui.tabs[1].restart_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.timeStarted = [None, None]
        self.timePaused = [None, None]
        self.isPaused = [False, False]
        print(self.timeStarted, self.timePaused, self.isPaused)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(50)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.draggable:
            if self.oldPos is None:
                self.oldPos = event.globalPos()
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def setDraggableState(self, state):
        if state == "Press":
            self.draggable = False
        elif state == "Leave":
            self.draggable = True

    def mouseoverEvent(self, event):
        if event == "Leave":
            self.prevSize = self.size()

            self.ui.tabs[self.curTab].button_frame.hide()
            if self.isBotFrameShown:
                self.ui.tabs[self.curTab].bot_frame.hide()

            self.resize(340, 92)
            self.setWindowOpacity(self.NO_FOCUS_OPACITY)

        elif event == "Enter":
            self.ui.tabs[self.curTab].button_frame.show()
            if self.isBotFrameShown:
                self.ui.tabs[self.curTab].bot_frame.show()

            self.resize(self.prevSize)
            self.setWindowOpacity(self.BASE_OPACITY)

    def nextTabBtnEvent(self):
        self.ui.tabs[self.curTab].hide()
        self.curTab = (self.curTab + 1) % len(self.ui.tabs)
        self.ui.tabs[self.curTab].show()

    def closeBtnEvent(self):
        self.close()

    def minimizeBtnEvent(self):
        self.showMinimized()

    def pauseBtnEvent(self, btn):
        if self.isPaused[self.curTab]:
            pauseTime = datetime.now() - self.timePaused[self.curTab]
            self.timeStarted[self.curTab] = self.timeStarted[self.curTab] + pauseTime
            self.isPaused[self.curTab] = False
            btn.setIcon(QtGui.QIcon(getcwd() + '\Icons\pause.png'))

        elif self.timeStarted[self.curTab]:
            self.timePaused[self.curTab] = datetime.now()
            self.isPaused[self.curTab] = True
            btn.setIcon(QtGui.QIcon(getcwd() + '\Icons\play-button-arrowhead.png'))

        else:
            self.timeStarted[self.curTab] = datetime.now()
            btn.setIcon(QtGui.QIcon(getcwd() + '\Icons\pause.png'))

    @QtCore.pyqtSlot(str)
    def flagClickedSlot(self, mouseBtnClicked):
        if mouseBtnClicked == "Left":
            # curFlag
            if self.timeStarted[self.curTab] is None:
                return
            if self.isPaused[self.curTab]:
                curFlag = self.timePaused[self.curTab] - self.timeStarted[self.curTab]
            else:
                curFlag = datetime.now() - self.timeStarted[self.curTab]

            # deltaTime
            if self.lastFlag is None or self.lastFlag == curFlag:
                deltaTime = str(timedelta())
            else:
                deltaTime = str(curFlag - self.lastFlag)
                deltaTime = deltaTime[:deltaTime.find(".") + 3]
            self.lastFlag = curFlag

            dTLable = QtWidgets.QLabel(deltaTime)
            dTLable.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(14)
            dTLable.setFont(font)
            dTLable.setStyleSheet(f"color: rgb({self.TEXT_COLOR});")

            self.ui.tabs[self.curTab].time_Layout.insertWidget(0, dTLable)

            # allTime
            allTime = str(curFlag)
            allTime = allTime[:allTime.find(".") + 3]
            aTLable = QtWidgets.QLabel(allTime)
            aTLable.setAlignment(QtCore.Qt.AlignCenter)
            aTLable.setFont(font)
            aTLable.setStyleSheet(f"color: rgb({self.TEXT_COLOR});")

            self.ui.tabs[self.curTab].all_Layout.insertWidget(0, aTLable)

        elif mouseBtnClicked == "Right":
            if self.isBotFrameShown:
                self.isBotFrameShown = False
                self.ui.tabs[self.curTab].bot_frame.hide()

                self.resize(340, 142)
                # self.setFixedSize(340, 142)

            else:
                self.isBotFrameShown = True
                self.resize(340, 300)
                self.ui.tabs[self.curTab].bot_frame.show()

    def restartBtnEvent(self):

        self.timeStarted[self.curTab] = None
        self.timePaused[self.curTab] = None
        self.isPaused[self.curTab] = False

        self.lastFlag = None

        for i in reversed(range(self.ui.tabs[self.curTab].time_Layout.count())):
            timeWidgetToRemove = self.ui.tabs[self.curTab].time_Layout.itemAt(i).widget()
            allWidgetToRemove = self.ui.tabs[self.curTab].all_Layout.itemAt(i).widget()
            # remove it from the layout list
            self.ui.tabs[self.curTab].time_Layout.removeWidget(timeWidgetToRemove)
            self.ui.tabs[self.curTab].all_Layout.removeWidget(allWidgetToRemove)
            # remove it from the gui
            timeWidgetToRemove.setParent(None)
            allWidgetToRemove.setParent(None)

        self.ui.tabs[self.curTab].pause_button.setIcon(QtGui.QIcon(getcwd() + '\Icons\play-button-arrowhead.png'))

    def showTime(self):
        if self.isPaused[self.curTab] is False:
            if self.timeStarted[self.curTab] is None:
                self.ui.tabs[self.curTab].timer.setText(str(timedelta()))
            else:
                t = str(datetime.now() - self.timeStarted[self.curTab])
                t = t[:t.find(".") + 3]
                self.ui.tabs[self.curTab].timer.setText(t)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TimerWindow()
    MainWindow.show()
    sys.exit(app.exec_())
