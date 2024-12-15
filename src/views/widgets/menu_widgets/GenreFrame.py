from PyQt5.QtWidgets import QFrame, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from src.utils.helpers import center_widget

class GenreFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        # position and size
        self.setFixedSize(530, 575)

        # status label
        self.status = QLabel("Genre tab is still in development", self)
        self.status.setFixedWidth(300)
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setWordWrap(True)
        self.status.setStyleSheet("color: black;")
        self.status.setFont(QFont("Itim", 20, QFont.Bold))

        # center the status label
        center_widget(self.status, self)

