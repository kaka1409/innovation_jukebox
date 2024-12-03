from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt

class CustomQFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Popup)
        self.setFocusPolicy(Qt.ClickFocus)  # Change to ClickFocus to ensure proper focus handling

    def focusOutEvent(self, event):
        """Hide the pop-up when it loses focus."""
        self.hide()  # Ensure the frame is hidden when focus is lost
        super().focusOutEvent(event)

