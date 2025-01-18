from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time


class SplashScreen(QWidget):
    def __init__(self, nextScreen):
        super().__init__()
        self.nextScreen = nextScreen
        self.setFixedSize(700, 350)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.counter = 0
        self.maxProgress = 100
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):

        # layout to display splash scrren frame
        layout = QVBoxLayout()
        self.setLayout(layout)

        # splash screen frame
        self.frame = QFrame()
        layout.addWidget(self.frame)

        # splash screen title
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName('title_label')
        self.title_label.resize(690, 120)
        self.title_label.move(0, 5)  # x, y
        self.title_label.setText('Knapsack')
        self.title_label.setAlignment(Qt.AlignCenter)

        # splash screen title description
        self.description_label = QLabel(self.frame)
        self.description_label.resize(690, 40)
        self.description_label.move(0, self.title_label.height())
        self.description_label.setObjectName('desc_label')
        self.description_label.setText('<b>Projet 2CS</b>')
        self.description_label.setAlignment(Qt.AlignCenter)

        # splash screen pogressbar
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, 180)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.maxProgress)
        self.progressBar.setValue(0)

        # spash screen loading label
        self.loading_label = QLabel(self.frame)
        self.loading_label.resize(self.width() - 10, 50)
        self.loading_label.move(0, self.progressBar.y() + 70)
        self.loading_label.setObjectName('loading_label')
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setText('Loading...')

    def loading(self):
        self.progressBar.setValue(self.counter)
        if self.counter >= self.maxProgress:
            self.timer.stop()
            self.close()
            time.sleep(1)
            self.nextScreen.show()
        self.counter += 1
