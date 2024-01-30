from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import QFrame, QLabel

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

        self.ui.tab_1.hide()
        self.ui.tab_0.show()

        self.ui.bot_frame.hide()
        self.ui.bot_frame_1.hide()

        self.cur_tab_ind = 0
        self.cur_tab = self.ui.tab_0
        self.cur_button_frame = self.ui.button_frame
        self.cur_bot_frame = self.ui.bot_frame
        self.cur_timer = self.ui.timer

        self.isBotFrameShown = False
        self.setMinimumSize(340, 94)
        self.resize(340, 142)  # 340, 142
        self.prevSize = self.size()
        self.oldPos = None
        self.draggable = True
        self.ui.centralwidget.mouseoverEvent.connect(lambda event: self.mouseoverEvent(event))

        self.ui.next_tab_button.clicked.connect(lambda: self.tabChange(self.ui.tab_1, self.ui.bot_frame_1, self.ui.button_frame_1, self.ui.timer_1, 1))
        self.ui.next_tab_button_1.clicked.connect(lambda: self.tabChange(self.ui.tab_0, self.ui.bot_frame, self.ui.button_frame, self.ui.timer, 0))
        self.ui.prev_tab_button.clicked.connect(lambda: self.tabChange(self.ui.tab_1, self.ui.bot_frame_1, self.ui.button_frame_1, self.ui.timer_1, 1))
        self.ui.prev_tab_button_1.clicked.connect(lambda: self.tabChange(self.ui.tab_0, self.ui.bot_frame, self.ui.button_frame, self.ui.timer, 0))
        self.ui.next_tab_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.next_tab_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.prev_tab_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.prev_tab_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.close_button.clicked.connect(lambda: self.closeBtnEvent())
        self.ui.close_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.close_button_1.clicked.connect(lambda: self.closeBtnEvent())
        self.ui.close_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.minimize_button.clicked.connect(lambda: self.minimizeBtnEvent())
        self.ui.minimize_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.minimize_button_1.clicked.connect(lambda: self.minimizeBtnEvent())
        self.ui.minimize_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.pause_button.clicked.connect(lambda: self.pauseBtnEvent(self.ui.pause_button))
        self.ui.pause_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.pause_button_1.clicked.connect(lambda: self.pauseBtnEvent(self.ui.pause_button_1))
        self.ui.pause_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.lastFlag = None
        self.ui.flag_button.clickedSignal.connect(self.flagClickedSlot)
        self.ui.flag_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.flag_button_1.clickedSignal.connect(self.flagClickedSlot)
        self.ui.flag_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.restart_button.clicked.connect(lambda: self.restartBtnEvent(self.ui.pause_button))
        self.ui.restart_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.restart_button_1.clicked.connect(lambda: self.restartBtnEvent(self.ui.pause_button_1))
        self.ui.restart_button_1.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.hours_up_button.clicked.connect(lambda: self.timerChoseHoursEvent(self.ui.hours_label, 1))
        self.ui.hours_up_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.minutes_up_button.clicked.connect(lambda: self.timerChoseEvent(self.ui.minutes_label, 1))
        self.ui.minutes_up_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.seconds_up_button.clicked.connect(lambda: self.timerChoseEvent(self.ui.seconds_label, 1))
        self.ui.seconds_up_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.ui.hours_down_button.clicked.connect(lambda: self.timerChoseHoursEvent(self.ui.hours_label, -1))
        self.ui.hours_down_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.minutes_down_button.clicked.connect(lambda: self.timerChoseEvent(self.ui.minutes_label, -1))
        self.ui.minutes_down_button.draggedSignal.connect(lambda state: self.setDraggableState(state))
        self.ui.seconds_down_button.clicked.connect(lambda: self.timerChoseEvent(self.ui.seconds_label, -1))
        self.ui.seconds_down_button.draggedSignal.connect(lambda state: self.setDraggableState(state))

        self.timeStarted = [None, None]
        self.timePaused = [None, None]
        self.isPaused = [False, False]

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(50)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.draggable:
            if self.oldPos is None:
                self.oldPos = event.globalPos()
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        super().mouseMoveEvent(event)

    def setDraggableState(self, state):
        if state == "Press":
            self.draggable = False
        elif state == "Leave":
            self.draggable = True

    def mouseoverEvent(self, event):
        if event == "Leave":
            self.prevSize = self.size()

            self.cur_button_frame.hide()
            if self.isBotFrameShown:
                self.cur_bot_frame.hide()

            self.resize(340, 94)
            self.setWindowOpacity(self.NO_FOCUS_OPACITY)

        elif event == "Enter":
            self.cur_button_frame.show()
            if self.isBotFrameShown:
                self.cur_bot_frame.show()

            self.resize(self.prevSize)
            self.setWindowOpacity(self.BASE_OPACITY)

    def tabChange(self, next_tab: QFrame, next_bot_frame: QFrame, next_button_frame: QFrame, next_timer: QLabel, ind: int) -> None:
        self.cur_tab.hide()
        next_tab.show()
        if self.isBotFrameShown:
            next_bot_frame.show()
        else:
            next_bot_frame.hide()

        self.cur_tab = next_tab
        self.cur_bot_frame = next_bot_frame
        self.cur_button_frame = next_button_frame
        self.cur_timer = next_timer
        self.cur_tab_ind = ind

    def closeBtnEvent(self):
        self.close()

    def minimizeBtnEvent(self):
        self.showMinimized()

    def pauseBtnEvent(self, btn):
        if self.isPaused[self.cur_tab_ind]:
            pauseTime = datetime.now() - self.timePaused[self.cur_tab_ind]
            self.timeStarted[self.cur_tab_ind] = self.timeStarted[self.cur_tab_ind] + pauseTime
            self.isPaused[self.cur_tab_ind] = False
            btn.setIcon(QtGui.QIcon(getcwd() + '\Icons\pause.png'))

        elif self.timeStarted[self.cur_tab_ind]:
            self.timePaused[self.cur_tab_ind] = datetime.now()
            self.isPaused[self.cur_tab_ind] = True
            btn.setIcon(QtGui.QIcon(getcwd() + '\Icons\play-button-arrowhead.png'))

        else:
            self.timeStarted[self.cur_tab_ind] = datetime.now()
            btn.setIcon(QtGui.QIcon(getcwd() + '\Icons\pause.png'))

    @QtCore.pyqtSlot(str)
    def flagClickedSlot(self, mouseBtnClicked):
        if mouseBtnClicked == "Left":
            # curFlag
            if self.timeStarted[self.cur_tab_ind] is None:
                return
            if self.isPaused[self.cur_tab_ind]:
                curFlag = self.timePaused[self.cur_tab_ind] - self.timeStarted[self.cur_tab_ind]
            else:
                curFlag = datetime.now() - self.timeStarted[self.cur_tab_ind]

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

            self.ui.time_layout.insertWidget(0, dTLable)

            # allTime
            allTime = str(curFlag)
            allTime = allTime[:allTime.find(".") + 3]
            aTLable = QtWidgets.QLabel(allTime)
            aTLable.setAlignment(QtCore.Qt.AlignCenter)
            aTLable.setFont(font)
            aTLable.setStyleSheet(f"color: rgb({self.TEXT_COLOR});")

            self.ui.all_layout.insertWidget(0, aTLable)

        elif mouseBtnClicked == "Right":
            if self.isBotFrameShown:
                self.isBotFrameShown = False
                self.cur_bot_frame.hide()

                self.resize(340, 142)
                # self.setFixedSize(340, 142)

            else:
                self.isBotFrameShown = True
                self.resize(340, 300)
                self.cur_bot_frame.show()

    def restartBtnEvent(self, pause_button) -> None:

        self.timeStarted[self.cur_tab_ind] = None
        self.timePaused[self.cur_tab_ind] = None
        self.isPaused[self.cur_tab_ind] = False

        self.lastFlag = None

        for i in reversed(range(self.ui.time_layout.count())):
            timeWidgetToRemove = self.ui.time_layout.itemAt(i).widget()
            allWidgetToRemove = self.ui.all_layout.itemAt(i).widget()
            # remove it from the layout list
            self.ui.time_layout.removeWidget(timeWidgetToRemove)
            self.ui.all_layout.removeWidget(allWidgetToRemove)
            # remove it from the gui
            timeWidgetToRemove.setParent(None)
            allWidgetToRemove.setParent(None)

        pause_button.setIcon(QtGui.QIcon(getcwd() + '\Icons\play-button-arrowhead.png'))

    def timerChoseHoursEvent(self, label: QLabel, increment: int) -> None:
        if label.text() == "00" and increment == -1:
            t = "23"
        elif label.text() == "23" and increment == 1:
            t = "00"
        else:
            t = f"{int(label.text()) + increment:02d}"
        label.setText(t)

    def timerChoseEvent(self, label: QLabel, increment: int) -> None:
        if label.text() == "00" and increment == -1:
            t = "59"
        elif label.text() == "59" and increment == 1:
            t = "00"
        else:
            t = f"{int(label.text()) + increment:02d}"
        label.setText(t)

    def showTime(self):
        if self.isPaused[self.cur_tab_ind] is False:
            if self.timeStarted[self.cur_tab_ind] is None:
                self.cur_timer.setText(str(timedelta()))
            else:
                t = str(datetime.now() - self.timeStarted[self.cur_tab_ind])
                t = t[:t.find(".") + 3]
                self.cur_timer.setText(t)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TimerWindow()
    MainWindow.show()
    sys.exit(app.exec_())
