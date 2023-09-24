import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, \
    QLCDNumber, QSlider, QVBoxLayout, QHBoxLayout, QPushButton


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.lcd = QLCDNumber(self)
        # Устанавливаем значение по умолчанию на дисплей
        self.lcd.display(1)

        self.slider = QSlider(Qt.Horizontal, self)
        # Устанавливаем минимальное и максимальное значение
        self.slider.setMinimum(1)
        self.slider.setMaximum(90)
        self.slider.valueChanged.connect(self.lcd.display)

        self.start_btn = QPushButton('Start', self)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        self.toggle_btns()

        hbox = QHBoxLayout()
        hbox.addWidget(self.slider)
        hbox.addWidget(self.start_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle('Timer PyQt5')
        self.resize(400, 300)

    def toggle_btns(self, value=True):
        self.slider.setEnabled(value)
        self.start_btn.setEnabled(value)

    def start_btn_clicked(self):
        # Отключаем слайдер и кнопку старта
        self.toggle_btns(False)
        # запускаем отсчет
        self.tick_timer()

    def tick_timer(self):
        # Получаем значение на LCD виджете
        lcd_value = self.lcd.value()
        if lcd_value > 0:
            # Устанавливаем значение на 1 меньше
            self.lcd.display(lcd_value - 1)
            # Засекаем таймер - значение в милисекундах
            # метод singleShot создает поток в фоне, отменить его нельзя
            QTimer().singleShot(1000, self.tick_timer)
        else:
            # Значение дисплея стало 0
            # Включаем элементы интерфейса обратно
            self.toggle_btns()
            # Устанавливаем на дисплей выбранную на слайдере настройку
            self.lcd.display(self.slider.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())