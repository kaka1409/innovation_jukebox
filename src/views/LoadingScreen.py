from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QFont

from src.utils.helpers import center_widget

class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(450, 300)

        # centering loading screen on the deskop
        center_widget(self)

        # init layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0 ,0)

        # create label to contain the GIF
        self.background = QLabel(self)
        self.background.setAlignment(Qt.AlignCenter)

        # load the GIF to the label
        self.gif = QMovie("assets/GIF/loading.gif")
        self.background.setMovie(self.gif)
        
        layout.addWidget(self.background)

        # title 
        self.title = QLabel("Loading, please wait ...", self)
        self.title.setFixedSize(275, 50)
        title_padding = (self.width() - self.title.width()) // 2
        self.title.move(title_padding, 20)
        self.title.setStyleSheet("color: white;")
        self.title.setFont(QFont("Poppins", 18, QFont.Bold))

        # start the gif
        self.gif.start()