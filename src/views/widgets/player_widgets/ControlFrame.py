from PyQt5.QtWidgets import QFrame, QHBoxLayout, QStackedLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class ControlFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.initProperties()
        self.styling()

    def initProperties(self):
        # position the frame
        self.setGeometry(20, 645, 525, 70)

        # init layout for the frame
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(65)

        # frame to contain play and pause button
        self.stack_button_frame = QFrame()
        self.stack_button_frame.setFixedSize(50, 50)

        # set stacked layout for button frame
        self.stack_button_frame.layout = QStackedLayout(self.stack_button_frame)

        # add control icons
        self.icon_paths = [
            "assets/icons/repeat.png", # repeat icon
            "assets/icons/repeat_off.png", # repeat off icon
            "assets/icons/previous.png", # previous icon
            "assets/icons/play.png", # play icon
            "assets/icons/pause.png", # pause icon
            "assets/icons/next.png", # next icon
            "assets/icons/shuffle.png", # shuffle icon
            "assets/icons/shuffle_off.png", # shuffle off icon
        ]

        # loop button
        self.loop_button = QPushButton(self)
        self.loop_button.setFixedSize(50, 50)
        self.loop_button.setIcon(QIcon(self.icon_paths[1]))
        self.loop_button.setIconSize(QSize(50, 50))
        self.loop_button.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(self.loop_button)
        self.is_looped = False

        # previous button
        self.previous_button = QPushButton(self)
        self.previous_button.setFixedSize(50, 50)
        self.previous_button.setIcon(QIcon(self.icon_paths[2]))
        self.previous_button.setIconSize(QSize(50, 50))
        self.previous_button.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(self.previous_button)

        # play button
        self.play_button = QPushButton(self)
        self.play_button.setFixedSize(50, 50)
        self.play_button.setIcon(QIcon(self.icon_paths[3]))
        self.play_button.setIconSize(QSize(50, 50))
        self.play_button.setCursor(Qt.PointingHandCursor)
        self.stack_button_frame.layout.addWidget(self.play_button)
        self.play_button.clicked.connect(self.let_go)

        # pause button
        self.pause_button = QPushButton(self)
        self.pause_button.setFixedSize(50, 50)
        self.pause_button.setIcon(QIcon(self.icon_paths[4]))
        self.pause_button.setIconSize(QSize(50, 50))
        self.pause_button.setCursor(Qt.PointingHandCursor)
        self.stack_button_frame.layout.addWidget(self.pause_button)

        # next button
        self.next_button = QPushButton(self)
        self.next_button.setFixedSize(50, 50)
        self.next_button.setIcon(QIcon(self.icon_paths[5]))
        self.next_button.setIconSize(QSize(50, 50))
        self.next_button.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(self.next_button)

        # shuffle button
        self.shuffle_button = QPushButton(self)
        self.shuffle_button.setFixedSize(50, 50)
        self.shuffle_button.setIcon(QIcon(self.icon_paths[7]))
        self.shuffle_button.setIconSize(QSize(50, 50))
        self.shuffle_button.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(self.shuffle_button)
        self.is_shuffled = False

        # add stack frame to layout
        self.layout.insertWidget(2, self.stack_button_frame)
        
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

        if self.is_looped:
            self.loop_button.setIcon(QIcon(self.icon_paths[1]))
            self.is_looped = False
        else:
            self.loop_button.setIcon(QIcon(self.icon_paths[0]))
            self.is_looped = True

    def update_shuffle_icon(self):
        """ change the shuffle icon of the button is clicked"""

        if not self.is_shuffled:
            self.shuffle_button.setIcon(QIcon(self.icon_paths[6]))
            self.is_shuffled = True
        else:
            self.shuffle_button.setIcon(QIcon(self.icon_paths[7]))
            self.is_shuffled = False

    def let_go(self):
        print("hello world")


    
            
    


        