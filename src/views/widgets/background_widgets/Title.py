from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class Title(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Create "JUKE" word
        self.juke_label = QLabel("JUKE", self)
        self.juke_label.setFont(QFont("Poppins", 80))
        self.juke_label.setStyleSheet("color: black;")
        self.juke_label.setAlignment(Qt.AlignRight)

        # Add shadow effect to "JUKE"
        juke_shadow = QGraphicsDropShadowEffect()
        juke_shadow.setBlurRadius(20)  # Smoothness of the shadow
        juke_shadow.setOffset(10, 10)  # Horizontal and vertical offsets
        juke_shadow.setColor(QColor(0, 0, 0, 100))  # dark
        self.juke_label.setGraphicsEffect(juke_shadow)

        # Create "BOX" word
        self.box_label = QLabel("BOX", self)
        self.box_label.setFont(QFont("Poppins", 80))
        self.box_label.setStyleSheet("color: white;")
        self.box_label.setAlignment(Qt.AlignLeft)

        # Add shadow effect to "BOX"
        box_shadow = QGraphicsDropShadowEffect()
        box_shadow.setBlurRadius(20)  # Smoothness of the shadow
        box_shadow.setOffset(-10, 10)  # Horizontal and vertical offsets
        box_shadow.setColor(QColor(255, 255, 255, 100))  #  white
        self.box_label.setGraphicsEffect(box_shadow)

    def resizeEvent(self, event):
        # Adjust the position and size of the labels based on the widget size
        
        total_width = self.width()
        mid_point = total_width // 2

        # Resize "JUKE" and "BOX" labels
        self.juke_label.setGeometry(10, 10, mid_point - 20, 120)
        self.box_label.setGeometry(mid_point + 10, 10, mid_point - 20, 120)
