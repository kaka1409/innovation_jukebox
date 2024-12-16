from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from src.views.widgets.custom_widgets.CustomQSilder import CustomQSilder

class ProgressBar(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.init_properties()
        self.init_children()
        self.init_appearance()

    def init_properties(self):
        # position the frame
        self.setGeometry(30, 565, 500, 70)

        # init layout for the frame
        self.layout = QHBoxLayout(self)
        self.setContentsMargins(25, 0, 25, 0)

    def init_children(self):

        # Song progress bar
        self.song_progress = CustomQSilder(Qt.Horizontal, self)
        self.song_progress.setRange(0, 200)
        self.song_progress.setValue(0)
        self.layout.addWidget(self.song_progress) # add to layout
        self.song_progress.is_programmic_changed = False

        # start time stamp
        default_current_time = "--:--"
        self.current_time = QLabel(default_current_time, self)
        self.current_time.setFont(QFont("Itim", 9, QFont.Light))
        self.current_time.setGeometry(6, 20, 30, 30)

        # start end stamp
        default_end_time = "--:--"
        self.end_time = QLabel(default_end_time, self)
        self.end_time.setFont(QFont("Itim", 9, QFont.Light))
        self.end_time.setGeometry(471, 20, 30, 30)

    def init_appearance(self):

        # naming the widgets to target them in QSS
        self.setObjectName("control_frame")
        self.song_progress.setObjectName("song_progress")
        self.current_time.setObjectName("start_time")
        self.end_time.setObjectName("end_time")

        # styling 
        self.setStyleSheet(
            """
                #control_frame {
                    margin: 0;
                    padding: 0 10px;
                }

                #start_time, #end_time {
                    margin: 0;
                    padding: 0;
                    color: white;
                }

                #song_progress::groove:horizontal {
                    border: none;
                    border-radius: 2px;
                    background: rgba(255, 255, 255, 0.3); 
                    height: 4px;         
                    margin: 0 -3px;  
                }

                #song_progress::handle:horizontal {
                    background: white;
                    border: 1px solid black;
                    width: 15px;
                    height: 15px;
                    padding: 0;
                    margin: -6px 0px;
                    border-radius: 8px;
                }

                #song_progress::sub-page:horizontal {
                    background: blue;
                    border-radius: 2px;   
                }

                #song_progress::add-page:horizontal{
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 2px;
                }

            """
        )

    def change_value(self, value):
        """
        change value of the QSilder using setValue() and update the state
        to differentiate from the change made by user
        """
        self.song_progress.is_programmic_changed = True 
        self.song_progress.setValue(value)
        self.song_progress.is_programmic_changed = False 


