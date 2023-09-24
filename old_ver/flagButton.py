from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta

from scrollWidget import ScrollWidget


class FlagButton(QtWidgets.QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self.lastFlag = None
        self.isShown = False
        # self.s = Example()
        # self.s.my_signal.connect(lambda x: ScrollWidget.buildScrollWidget(self.window(), x))

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            # curFlag
            if self.window().timeStarted is None:
                return
            if self.window().isPaused:
                self.curFlag = self.window().timePaused - self.window().timeStarted
            else:
                self.curFlag = datetime.now() - self.window().timeStarted

            # deltaTime
            if self.lastFlag is None or self.lastFlag == self.curFlag:
                deltaTime = str(timedelta())
            else:
                deltaTime = str(self.curFlag - self.lastFlag)
                deltaTime = deltaTime[:deltaTime.find(".") + 3]
            self.lastFlag = self.curFlag

            dTLable = QtWidgets.QLabel(deltaTime)
            dTLable.setAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(14)
            dTLable.setFont(font)
            dTLable.setStyleSheet(f"color: rgb({self.window().TEXT_COLOR});")

            deltaTimeLayout = self.window().ui.deltaTimeWidget.layout()
            deltaTimeLayout.insertWidget(0, dTLable)

            # allTime
            allTime = str(self.curFlag)
            allTime = allTime[:allTime.find(".") + 3]
            aTLable = QtWidgets.QLabel(allTime)
            aTLable.setAlignment(QtCore.Qt.AlignCenter)
            aTLable.setFont(font)
            aTLable.setStyleSheet(f"color: rgb({self.window().TEXT_COLOR});")

            allTimeLayout = self.window().ui.allTimeWidget.layout()
            allTimeLayout.insertWidget(0, aTLable)

        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            if self.isShown:
                self.isShown = False
                self.window().resize(340, 160)
            else:
                self.isShown = True
                self.window().resize(340, 320)

    def clearSliderWidget(self):
        self.lastFlag = None

        scrollwidgetLayout = self.window().ui.scrollwidget.layout()
        scrollwidgetLayout.removeWidget(self.window().ui.deltaTimeWidget)
        scrollwidgetLayout.removeWidget(self.window().ui.allTimeWidget)

        self.window().ui.deltaTimeWidget = QtWidgets.QWidget()
        self.window().ui.allTimeWidget = QtWidgets.QWidget()

        deltaTimeVBox, allTimeVBox = QtWidgets.QVBoxLayout(), QtWidgets.QVBoxLayout()
        self.window().ui.deltaTimeWidget.setLayout(deltaTimeVBox)
        self.window().ui.allTimeWidget.setLayout(allTimeVBox)

        scrollwidgetLayout.addWidget(self.window().ui.deltaTimeWidget)
        scrollwidgetLayout.addWidget(self.window().ui.allTimeWidget)
