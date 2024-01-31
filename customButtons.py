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
    __clickedLeftSig = QtCore.pyqtSignal()
    __clickedRightSig = QtCore.pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.clickedLeftSignal = self.__clickedLeftSig
        self.clickedRightSignal = self.__clickedRightSig

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clickedLeftSignal.emit()

        elif QMouseEvent.button() == QtCore.Qt.RightButton:
            self.clickedRightSignal.emit()
        super().mouseReleaseEvent(QMouseEvent)


class ScrollButton(NotDraggableButton):
    __releasedSig = QtCore.pyqtSignal()
    __pressSig = QtCore.pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.releasedSignal = self.__releasedSig
        self.pressSignal = self.__pressSig

    def mouseReleaseEvent(self, QMouseEvent):
        self.releasedSignal.emit()
        super().mouseReleaseEvent(QMouseEvent)

    def mousePressEvent(self, QMouseEvent):
        self.pressSignal.emit()
        super().mousePressEvent(QMouseEvent)
