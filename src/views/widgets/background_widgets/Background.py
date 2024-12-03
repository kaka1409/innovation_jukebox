import sys

from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPainter, QPixmap, QFont, QColor
from PyQt5.QtCore import Qt, QRect

class Background(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Load the background images
        self.left_background = QPixmap("assets/images/background_images/light_background.png")
        self.right_background = QPixmap("assets/images/background_images/dark_background.png")
    
    def paintEvent(self, event):
        # init painter
        painter = QPainter(self)
        
        # Calculate dimensions for split background
        total_width = self.width()
        height = self.height()
        mid_point = total_width // 2
        
        # Draw left background
        painter.drawPixmap(QRect(0, 0, mid_point + 2, height), self.left_background)
        # Draw right background
        painter.drawPixmap(QRect(mid_point, 0, mid_point + 2, height), self.right_background)