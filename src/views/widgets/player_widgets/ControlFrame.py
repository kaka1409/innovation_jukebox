from PyQt5.QtWidgets import QFrame, QHBoxLayout, QStackedLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class ControlFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.initProperties()
        self.init_childern()
        self.styling()

    def initProperties(self):
        # position the frame
        self.setGeometry(20, 645, 525, 70)

        # init layout for the frame
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(66)

        # frame to contain play and pause button
        self.stack_button_frame = QFrame()
        self.stack_button_frame.setFixedSize(50, 50)

        # set stacked layout for button frame
        self.stack_button_frame.layout = QStackedLayout(self.stack_button_frame)

    def init_childern(self):

        # list of icon paths
        self.icon_paths = {
            "repeat": "assets/icons/repeat.png",  # loop button on
            "repeat_off": "assets/icons/repeat_off.png",  # loop button off
            "previous": "assets/icons/previous.png",  # previous button
            "play": "assets/icons/play.png",  # play button
            "pause": "assets/icons/pause.png",  # pause button
            "next": "assets/icons/next.png",  # next button
            "shuffle": "assets/icons/shuffle.png",  # shuffle button on
            "shuffle_off": "assets/icons/shuffle_off.png"  # shuffle button off
        }

        # buttons
        self.loop_button = QPushButton(self)
        self.previous_button = QPushButton(self)
        self.play_button = QPushButton(self)
        self.pause_button = QPushButton(self)
        self.next_button = QPushButton(self)
        self.shuffle_button = QPushButton(self)
        
        # flags
        self.is_looped = False
        self.is_shuffled = False

        # init buttons properties
        self.init_buttons_properties(
            {
                "repeat": self.loop_button,
                "previous": self.previous_button,
                "play": self.play_button,
                "pause": self.pause_button,
                "next": self.next_button,
                "shuffle": self.shuffle_button
            }
        )

        # add stack frame to layout
        self.layout.insertWidget(2, self.stack_button_frame)

    def init_buttons_properties(self, buttons_dictionary):

        for button_key in buttons_dictionary:

            # get the button from the dictionary
            button = buttons_dictionary[button_key]

            # set button properties
            button.setFixedSize(50, 50)
            button.setIcon(QIcon(self.icon_paths[button_key]))
            button.setIconSize(QSize(50, 50))
            button.setCursor(Qt.PointingHandCursor)

            # set loop button and shuffle button to off as default
            if button_key in ["repeat", "shuffle"]:
                button.setIcon(QIcon(self.icon_paths[button_key + "_off"]))

            # add buttons to appropriate layout
            if button_key in ["play", "pause"]: 
                self.stack_button_frame.layout.addWidget(button)
            else:
                self.layout.addWidget(button)
        
    def styling(self):
        # styling the frame
        self.setObjectName("control_frame")
        self.setStyleSheet(
            """
                #control_frame {
                    padding: 0;
                    margin: 0;
                }

                QPushButton {
                    border-radius: 15px; 
                    padding: 0;
                    margin: 0;
                    background-color: rgba(0, 0, 0, 0);
                    border: 0px;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.2)
                }
            """
        )

    def update_loop_icon(self):
        """ change the loop icon of the button is clicked"""

        if not self.is_looped:
            self.loop_button.setIcon(QIcon(self.icon_paths["repeat"]))
            self.is_looped = True
        else:
            self.loop_button.setIcon(QIcon(self.icon_paths["repeat_off"]))
            self.is_looped = False

    def update_shuffle_icon(self):
        """ change the shuffle icon of the button is clicked"""

        if not self.is_shuffled:
            self.shuffle_button.setIcon(QIcon(self.icon_paths["shuffle"]))
            self.is_shuffled = True
        else:
            self.shuffle_button.setIcon(QIcon(self.icon_paths["shuffle_off"]))
            self.is_shuffled = False



    
            
    


        