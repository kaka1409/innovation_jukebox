from PyQt5.QtWidgets import QPushButton, QFrame, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QPoint

from src.utils.helpers import get_text_width

class TabsFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.init_properties()
        self.init_children()
        self.init_appearance()

    def init_properties(self):

        self.setGeometry(25, 70, 488, 60)

        # init layout of the frame 
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(30)

    def init_children(self):

        # line
        self.indicator = QFrame(self)
        self.indicator.setStyleSheet("background-color: black;")
        self.indicator.setFixedHeight(2)  
        self.indicator.setGeometry(12, 45, 50, 2)  
        
        # Initialize all tabs
        self.song_tab = QPushButton("Song")
        self.playlist_tab = QPushButton("Playlist")
        self.favorite_tab = QPushButton("Favorite")
        self.genre_tab = QPushButton("Genre")
        self.artist_tab = QPushButton("Artist")

        # define all tabs's necessary properties
        self.init_tab_properties(
            {
                "song_tab": self.song_tab,
                "playlist_tab": self.playlist_tab,
                "favorite_tab": self.favorite_tab,
                "genre_tab": self.genre_tab,
                "artist_tab": self.artist_tab
            }
        )  

        # init moving line animation
        self.moving_line_animation = QPropertyAnimation(self.indicator, b"geometry")
        self.moving_line_animation.setDuration(150)  #  duration

    def init_tab_properties(self, tab_dictionary):

        # selected button
        self.selected_tab = None  

        # tab font
        self.selected_tab_font = QFont("Itim", 14, QFont.Bold)
        self.not_selected_tab_font = QFont("Itim", 14, QFont.Light)

        for index, tab in enumerate(tab_dictionary):

            # create the button
            tab_btn = tab_dictionary[tab]
            tab_btn.tab_index = index

            tab_btn.setFont(self.not_selected_tab_font)
            tab_btn.setCursor(Qt.PointingHandCursor)

            # set song tab is selected as default
            if tab == "Song": 
                self.selected_tab = tab_btn
                self.selected_tab.setFont(self.selected_tab_font)

            # Add button to layout
            self.layout.addWidget(tab_btn)

            # click event
            tab_btn.clicked.connect(lambda _, btn = tab_btn: self.select_tab(btn))

    def select_tab(self, selected_tab_btn):

        # Reset the previous tab
        if self.selected_tab is not None:
            self.selected_tab.setFont(self.not_selected_tab_font)

        # Update the font of the currently selected button
        selected_tab_btn.setFont(self.selected_tab_font)

        # set the currently selected button
        self.selected_tab = selected_tab_btn

        # move indicator under the selected tab
        self.move_indicator()

    def move_indicator(self):
        """Move the line under the selected tab"""

        # get necessary widgets
        selected_tab = self.selected_tab
        line = self.indicator
        line_animation = self.moving_line_animation

        text_width = get_text_width(selected_tab)  # get text width
        line_padding = (selected_tab.width() - text_width) // 2 # get line padding
        tab_pos = selected_tab.mapToParent(QPoint(0, 0)) # Get global position of the tab

        # Set start and end values for the animation
        start_value = line.geometry()
        end_value = QRect(tab_pos.x() + line_padding, 45, text_width, 2)

        line_animation.setStartValue(start_value)
        line_animation.setEndValue(end_value)
        line_animation.start()

    def init_appearance(self):

        self.setObjectName("tabs_frame")
        self.setStyleSheet(
            """
                #tabs_frame {
                    padding: 0;
                    margin: 0;
                }

                QPushButton {
                    color: rgb(0, 0, 0);
                    background-color: rgba(0, 0, 0, 0);
                    border: none;
                    padding: 0;
                    margin: 0;
                    max-width: 75px;
                }   

                QPushButton:hover {
                    font-weight: 500;
                    font-size: 13.5px;
                } 
            """
        )




