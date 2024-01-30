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
    __clickedSig = QtCore.pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.clickedSignal = self.__clickedSig

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clickedSignal.emit("Left")

        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            self.clickedSignal.emit("Right")
        super().mouseReleaseEvent(QMouseEvent)
