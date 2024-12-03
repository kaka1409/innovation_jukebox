from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt

class CustomQSilder(QSlider):
    def __init__(self, orientation = None, parent = None):
        super().__init__(orientation, parent)

        self.player_container = self.parent().parent()

    # overiding mouse click event
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Calculate the clicked position as a proportion of the slider's width
            pos = event.pos()
            if self.orientation() == Qt.Horizontal:
                new_value = self.minimum() + (self.maximum() - self.minimum()) * pos.x() / self.width()
            # else:  # For vertical sliders
            #     new_value = self.minimum() + (self.maximum() - self.minimum()) * (self.height() - pos.y()) / self.height()

            self.setValue(int(new_value))  # Set the slider value immediately
            event.accept()
        super().mousePressEvent(event)  # Continue with default behavior
    
    # overiding mouse release event
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:  # Left mouse button

            play_button = self.player_container.control_frame.play_button
            play_button.click()

            progress_bar = self.player_container.progress_bar.song_progress

            # user skip straigt to the end
            if progress_bar.value() == self.maximum():
                
                # click nexy button
                next_button = self.player_container.control_frame.next_button
                next_button.click()

                play_button.click()
