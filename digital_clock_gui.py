#Digital Clock
import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700, 700, 400, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                       "color: #17fc03;")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("/home/lonicero/Documents/vault/03-Coding/Python Projects/digit_clock/DS-DIGIT.ttf")
        if font_id == -1:
            print("Failed to load font. Check the file path")
        else:
         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
         custom_font = QFont(font_family, 150)
         self.time_label.setFont(custom_font)


        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    digital_clock = Digital_Clock()
    digital_clock.show()
    sys.exit(app.exec_())
