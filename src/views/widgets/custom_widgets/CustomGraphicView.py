from PyQt5.QtWidgets import QGraphicsView

# overiding the mouse's scroll wheel event
class CustomGraphicsView(QGraphicsView):
    def __init__(self, parent = None):
        super().__init__(parent)

    def wheelEvent(self, event):
        # Ignore the scroll event to prevent scrolling
        event.ignore()