from PyQt5 import QtCore, QtWidgets


class MouseoverWidget(QtWidgets.QWidget):
    __sig = QtCore.pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.mouseoverEvent = self.__sig

    def enterEvent(self, event):
        self.mouseoverEvent.emit("Enter")

    def leaveEvent(self, event):
        self.mouseoverEvent.emit("Leave")
