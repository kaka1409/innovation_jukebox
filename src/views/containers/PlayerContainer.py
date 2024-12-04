from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout, QSlider
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect

from src.views.widgets.player_widgets.ControlFrame import ControlFrame
from src.views.widgets.player_widgets.OptionsFrame import OptionsFrame
from src.views.widgets.player_widgets.Thumbnail import Thumbnail
from src.views.widgets.player_widgets.ProgressBar import ProgressBar

class PlayerContainer(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        # set the size right after the window is created
        self.setGeometry(800, 130, 560, 830)
        
        # get player frame width
        player_width = self.width()

        # init layout
        self.layout = QHBoxLayout(self)

        # Status
        self.status = QLabel("Now Playing")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("color: white") # font color
        self.status.setFont(QFont("Itim", 17, QFont.Light)) # font family, font weight, font weight
        self.status.setFixedSize(200, 50)
        status_padding = (player_width - self.status.width()) // 2 # centering the label
        self.status.move(status_padding, 25)
        self.status.setParent(self) # append

        # Song name
        song_name = "A new kind of love" # example song name
        self.song_name = QLabel(song_name)
        self.song_name.setAlignment(Qt.AlignCenter)
        self.song_name.setStyleSheet("color: white") # font color
        self.song_name.setFont(QFont("Itim", 25, QFont.Bold)) # font family, font size, font weight
        self.song_name.setFixedSize(300, 50)
        name_padding = (player_width - self.song_name.width()) // 2 # centering the label
        self.song_name.move(name_padding, 80)
        self.song_name.setParent(self) # append

        # Artist name
        artist_name = "Frou Frou" # example artist name
        self.artist_name = QLabel(artist_name)
        self.artist_name.setAlignment(Qt.AlignCenter)
        self.artist_name.setStyleSheet("color: white") # font color
        self.artist_name.setFont(QFont("Itim", 14, QFont.Light)) # font family, font size, font weight
        self.artist_name.setFixedSize(300, 50)
        artist_padding = (player_width - self.artist_name.width()) // 2 # centering the label
        self.artist_name.move(artist_padding, 120)
        self.artist_name.setParent(self) # append

        # Song thumnail
        self.thumbnail = Thumbnail(self)

        # Progress bar
        self.progress_bar = ProgressBar(self)

        # add control frame to the player container
        self.control_frame = ControlFrame(self)

        # add options frame to the player container
        self.options_frame = OptionsFrame(self)

        # connect volume icon click event in option frame to volume animation
        self.options_frame.volume_off_icon.clicked.connect(self.volume_bar_animation)
        self.options_frame.volume_not_full_icon.clicked.connect(self.volume_bar_animation)
        self.options_frame.volume_full_icon.clicked.connect(self.volume_bar_animation)

        # volume bar frame
        self.volume_bar_frame = QFrame(self)
        self.volume_bar_frame.setObjectName("volume_frame")
        self.volume_bar_frame.setGeometry(500, 325, 50, 0) # position
        
        # not visible as default
        self.is_volume_bar_visible = False

        # volume bar frame layout
        self.volume_bar_frame.layout = QVBoxLayout(self.volume_bar_frame)
        self.volume_bar_frame.layout.setContentsMargins(0, 0, 0, 0)

        # volume bar
        self.volume_bar = QSlider(Qt.Vertical)
        self.volume_bar.setRange(0, 100)
        self.volume_bar.setValue(80)
        self.volume_bar.setInvertedAppearance(True)
        self.volume_bar.setObjectName("volume_bar")
        self.volume_bar.setMinimumHeight(125)
        self.volume_bar_frame.layout.addWidget(self.volume_bar)
        self.volume_bar_frame.layout.setAlignment(self.volume_bar, Qt.AlignCenter)

        #volume bar animation
        self.volume_animation = QPropertyAnimation(self.volume_bar_frame, b'geometry')
        self.volume_animation.setDuration(300) # duration
        self.volume_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.setObjectName("player_container")
        self.setStyleSheet(
            """
                #player_container {
                    border-top-left-radius: 60px;
                    border-bottom-left-radius: 60px;
                    background: qlineargradient(
                        x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 rgba(50, 14, 142, 0.8),   
                        stop: 0.8 rgba(0, 0, 0, 0.9)    
                    );
                }

                #volume_frame {
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 25px;
                }

                #volume_bar::groove:vertical {
                    background: rgba(255, 255, 255, 0.1);
                    width: 4px;
                    border-radius: 2px;
                }

                #volume_bar::handle:vertical {
                    background: white;
                    border: none;
                    height: 10px;
                    width: 10px;
                    margin: 0 -3px;
                    border-radius: 5px;
                }

                #volume_bar::add-page:vertical {
                    background: rgba(255, 255, 255, 0.3);;
                    border-radius: 2px;
                }

                #volume_bar::sub-page:vertical {
                    background: rgba(0, 0, 255, 0.6);
                    border-radius: 2px;
                }
            """
        )

    def volume_bar_animation(self):
        """function called when volume button is clicked"""

        # volume bar animation
        animation = self.volume_animation
        isVisible = self.is_volume_bar_visible
        volume_bar_height = self.volume_bar_frame.height()

        if not isVisible:
            toggle_height = 150
        else:
            toggle_height = 0

        # start animation
        animation.setStartValue(QRect(500, 325, 50, volume_bar_height))
        animation.setEndValue(QRect(500, 325, 50, toggle_height))
        animation.start()

        # update state
        self.is_volume_bar_visible = not isVisible
