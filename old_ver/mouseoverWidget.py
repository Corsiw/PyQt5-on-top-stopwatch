from PyQt5 import QtCore, QtWidgets


class MouseoverWidget(QtWidgets.QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.prevSize = None

    def enterEvent(self, event):
        if self.prevSize:
            self.window().resize(self.prevSize)
            self.window().setWindowOpacity(self.window().BASE_OPACITY)

    def leaveEvent(self, event):
        self.prevSize = self.window().size()
        self.window().resize(340, 105)
        self.window().setWindowOpacity((self.window().NO_FOCUS_OPACITY))
