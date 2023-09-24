from PyQt5 import QtCore, QtWidgets


class NotDraggableButton(QtWidgets.QPushButton):
    __draggedSig = QtCore.pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.draggedSignal = self.__draggedSig

    def mousePressEvent(self, QMouseEvent):
        self.draggedSignal.emit("Press")
        super().mousePressEvent(QMouseEvent)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.draggedSignal.emit("Leave")
        super().leaveEvent(a0)


class FlagButton(NotDraggableButton):
    __sig = QtCore.pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.clickSignal = self.__sig

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clickSignal.emit("Left")

        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            self.clickSignal.emit("Right")
