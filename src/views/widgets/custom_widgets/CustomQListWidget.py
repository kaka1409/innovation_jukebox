from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import Qt

class CustomQListWidget(QListWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)

    def wheelEvent(self, event):
        """Disable user's scrolling event by mouse"""
        event.ignore()

    def focusOutEvent(self, event):
        """Hide the pop-up when it loses focus."""
        if not self.underMouse():
            self.hide()
        super().focusOutEvent(event)