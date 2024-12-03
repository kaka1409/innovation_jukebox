from PyQt5.QtWidgets import QFrame, QStackedLayout

from src.views.widgets.menu_widgets.SearchBar import SearchBar
from src.views.widgets.menu_widgets.TabsFrame import TabsFrame
from src.views.widgets.menu_widgets.SongListFrame import SongListFrame
from src.views.widgets.menu_widgets.PlayListFrame import PlayListFrame
from src.views.widgets.menu_widgets.FavoriteFrame import FavoriteFrame
from src.views.widgets.menu_widgets.GenreFrame import GenreFrame
from src.views.widgets.menu_widgets.ArtistFrame import ArtistFrame
from src.views.widgets.menu_widgets.MenuFooter import MenuFooter

class Menu(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        # add search bar to menu frame
        self.search_bar = SearchBar(self)

        # add tabs to menu frame
        self.tabs_frame = TabsFrame(self)

        # stacked layout for tabs
        self.stacked_tabs = QFrame(self)
        self.stacked_tabs.setGeometry(20, 140, 530, 575) 
        self.stacked_tabs.layout = QStackedLayout()

        # song list frame tab
        self.song_list_frame = SongListFrame(self.stacked_tabs)
        self.stacked_tabs.layout.addWidget(self.song_list_frame)
        self.stacked_tabs.layout.setCurrentIndex(0) # display song list (first tab) as default

        # playlist frame
        self.playlist_frame = PlayListFrame(self.stacked_tabs)
        self.stacked_tabs.layout.addWidget(self.playlist_frame)

        # Favorite frame
        self.favorite_frame = FavoriteFrame(self.stacked_tabs)
        self.stacked_tabs.layout.addWidget(self.favorite_frame)

        # Genre frame
        self.genre_frame = GenreFrame(self.stacked_tabs)
        self.stacked_tabs.layout.addWidget(self.genre_frame)

        # Artist frame
        self.artist_frame = ArtistFrame(self.stacked_tabs)
        self.stacked_tabs.layout.addWidget(self.artist_frame)

        # add footer frame to menu frame
        self.menu_footer = MenuFooter(self)
        
        # connect button click events to swicth tab in QStackedlayout
        # song button
        song_button = self.tabs_frame.tab_buttons[0]
        song_button.clicked.connect(lambda: self.select_song_tab(song_button.tab_index))
        
        # playlist button
        playlist_button = self.tabs_frame.tab_buttons[1]
        playlist_button.clicked.connect(lambda: self.select_song_tab(playlist_button.tab_index))

        # favorite button
        favorite_button = self.tabs_frame.tab_buttons[2]
        favorite_button.clicked.connect(lambda: self.select_song_tab(favorite_button.tab_index))

        # genre button
        genre_button = self.tabs_frame.tab_buttons[3]
        genre_button.clicked.connect(lambda: self.select_song_tab(genre_button.tab_index))

        # artist button
        artist_button = self.tabs_frame.tab_buttons[4]
        artist_button.clicked.connect(lambda: self.select_song_tab(artist_button.tab_index))

        # set the size right after the window is created
        self.setGeometry(800, 130, 560, 800)

        # call styling properties
        self.styling()

    def styling(self):
        """styling the frame"""

        self.setObjectName("menu")
        self.setStyleSheet(
            """
                #menu {
                    border-top-right-radius: 60px;
                    border-bottom-right-radius: 60px;
                    background: qlineargradient(
                        x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 rgba(255, 255, 255, 0.7),
                        stop: 0.5 rgba(188, 148, 195, 0.7),   
                        stop: 1 rgba(169, 82, 157, 0.7)    
                    );
                }
            """
        )

    def select_song_tab(self, current_tab_index):
        """Display the content of the selected tab"""

        self.stacked_tabs.layout.setCurrentIndex(current_tab_index)



