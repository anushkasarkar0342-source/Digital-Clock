
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initui()

    def initui(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 500, 150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font-size: 50px;"
            "color: green;"
        )

        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")

        if font_id != -1:
            font_families = QFontDatabase.applicationFontFamilies(font_id)

            if font_families:
                my_font = QFont(font_families[0], 50)
                self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    clock = DigitalClock()
    clock.show()

    sys.exit(app.exec_())
