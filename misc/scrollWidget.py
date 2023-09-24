from PyQt5 import QtCore, QtWidgets



class ScrollWidget:
    @staticmethod
    def buildScrollWidget(MainWindow, flags=None) -> None:
        print(MainWindow, flags)
        if flags is None:
            flags = []

        print(MainWindow.scroll)
        MainWindow.scroll = QtWidgets.QScrollArea(MainWindow.ui.centralwidget)
        MainWindow.scroll.setGeometry(QtCore.QRect(0, 160, 340, 160))
        MainWindow.scrollwidget = QtWidgets.QWidget(MainWindow.ui.centralwidget)

        MainWindow.deltaTimeWidget = QtWidgets.QWidget()
        MainWindow.allTimeWidget = QtWidgets.QWidget()

        MainWindow.box = QtWidgets.QHBoxLayout()
        MainWindow.deltaTimeVBox, MainWindow.allTimeVBox = QtWidgets.QVBoxLayout(), QtWidgets.QVBoxLayout()

        MainWindow.deltaTimeVBox.addWidget(QtWidgets.QLabel("Время"))
        MainWindow.allTimeVBox.addWidget(QtWidgets.QLabel("Итого"))
        if len(flags) >= 1:
            MainWindow.deltaTimeVBox.addWidget(QtWidgets.QLabel(str(flags[0])))
            MainWindow.allTimeVBox.addWidget(QtWidgets.QLabel(str(flags[0])))

        for i in range(1, len(flags)):
            object1 = QtWidgets.QLabel(str(flags[i] - flags[i - 1]))
            object2 = QtWidgets.QLabel(str(flags[i]))
            MainWindow.deltaTimeVBox.addWidget(object1)
            MainWindow.allTimeVBox.addWidget(object2)

        MainWindow.deltaTimeWidget.setLayout(MainWindow.deltaTimeVBox)
        MainWindow.allTimeWidget.setLayout(MainWindow.allTimeVBox)

        MainWindow.box.addWidget(MainWindow.deltaTimeWidget)
        MainWindow.box.addWidget(MainWindow.allTimeWidget)
        MainWindow.scrollwidget.setLayout(MainWindow.box)

        # Scroll Area Properties
        MainWindow.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        MainWindow.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        MainWindow.scroll.setWidgetResizable(True)
        MainWindow.scroll.setWidget(MainWindow.scrollwidget)


