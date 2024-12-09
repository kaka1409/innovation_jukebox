from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainterPath, QRegion
from PyQt5.QtCore import Qt, QSize

from src.utils.helpers import center_widget

class SongListFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.initProperties() # init the frame(layout, size, ...)
        self.init_children() # init all necessary widgets
        self.styling() # styling the frame and widgets

    def initProperties(self):
        
        # position and size
        self.setFixedSize(530, 575)

        # main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def init_children(self):
        # Song list
        self.song_list = QListWidget(self)
        self.song_list.setVerticalScrollMode(QListWidget.ScrollPerPixel) # scroll smoother
        self.song_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.song_list.setUniformItemSizes(True)
        self.song_list.setFocusPolicy(Qt.NoFocus)
        self.song_list.setObjectName("song_list")
        self.song_list.setFixedWidth(525)

        # scroll bar of the song list
        scrollbar = self.song_list.verticalScrollBar()
        scrollbar.setObjectName("scrollbar")

        # no song found message
        self.message = QLabel("Sadly! no song has been found :/", self)
        self.message.setFixedSize(250, 100)
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setStyleSheet("color: black;")
        self.message.setFont(QFont("Itim", 18, QFont.Bold))
        self.message.raise_()

        # set the message not visible as default
        self.message.setVisible(False)

        # center the message
        center_widget(self.message, self)
        
        self.layout.addWidget(self.song_list)

    def create_song_frame(self, song_name, artist, thumbnail = ""):

        song_frame = QFrame()

        # frame box with shadow
        song_frame.setFrameStyle(QFrame.Box)
        song_frame.setLineWidth(0)
        song_frame.setCursor(Qt.PointingHandCursor)
        song_frame.setMaximumSize(480, 110)
        song_frame.setObjectName("song_frame")

        # layout
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 0, 0, 0) # left, top, right, bottom
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)
        song_frame.setLayout(layout)

        # add song thumbnail frame
        song_thumbnail = QFrame(song_frame)
        song_thumbnail.setMaximumSize(60, 60)
        song_thumbnail.setMinimumSize(60, 60)
        layout.addWidget(song_thumbnail)

        # image container
        image_holder = QLabel(song_thumbnail)
        image_holder.setFixedSize(60, 60)
        image_holder.setAlignment(Qt.AlignCenter)
        image_holder.setPixmap(QPixmap(thumbnail).scaled(
                image_holder.width(),
                image_holder.height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )

        # crop the thumbnail image (using mask)
        path = QPainterPath()
        path.addRoundedRect(0, 0, 60, 60, 17, 17)
        region = QRegion(path.toFillPolygon().toPolygon())
        image_holder.setMask(region)

        # add song content frame
        song_content_frame = QFrame(song_frame)
        song_content_frame.setFixedSize(350, 60)
        song_content_frame.setObjectName("song_content_frame")

        # song name
        song_name = QLabel(song_name, song_content_frame)
        song_name.move(20, 5)
        song_name.setFont(QFont("Itim", 15, QFont.Bold))
        song_name.setObjectName("song_name")

        # song artist
        song_artist = QLabel(artist, song_content_frame)
        song_artist.move(20, 35)
        song_artist.setFont(QFont("Itim", 12))
        song_artist.setObjectName("song_artist")

        layout.addWidget(song_content_frame)

        # add more options
        more_button = QPushButton()
        more_button.setIcon(QIcon("assets/icons/more.png"))
        more_button.setIconSize(QSize(30, 30))
        more_button.setObjectName("more_button")
        layout.addWidget(more_button)

        return song_frame

    def add_song_frame(self, song_frame, song_object):
        
        # create list item
        song_item = QListWidgetItem(self.song_list)

        # set size for list item
        song_item.setSizeHint(song_frame.size())

        # set song object associated with song QListWidgetItem
        song_item.object_key = song_object

        # add item to song list
        self.song_list.addItem(song_item)
        self.song_list.setItemWidget(song_item, song_frame)

    def check_list_is_visible(self):
        """function to check whether all songs in the list is hidden"""

        # flag
        is_visible = True

        song_list = self.song_list
        song_list_length = song_list.count()

        for index in range(song_list_length):

            song_item = song_list.item(index)

            # is the loop detect 1 song is not hidden the flag will be changed
            if not song_item.isHidden():
                is_visible = False

        return is_visible

    def styling(self):
        self.setObjectName("song_list_frame")
        self.setStyleSheet(
            """
                #song_list_frame {
                    margin: 0;
                    padding: 0;
                }

                #song_list {
                    margin: 0;
                    padding: 0;
                    padding-right: 15px;
                    background-color: rgba(0, 0, 0, 0);
                    border: none;
                }

                #song_list::item {
                    outline: none;
                    padding: 0;
                    margin: 5px 0;
                    border-radius: 15px;
                }

                #song_list::item:hover {
                    border: none;
                    background-color: rgba(255, 255, 255, 0.1);
                }

                #song_list::item:selected {
                    border: none;
                    background-color: rgba(255, 255, 255, 0.4);

                }

                QScrollBar#scrollbar:vertical {
                    border: none;
                    background: rgba(200, 200, 200, 00);
                    min-width: 15px;      
                    padding-left: 5px;
                }

                QScrollBar#scrollbar::handle:vertical {
                    background: rgba(255, 255, 255, 0.5);
                    border-radius: 6px;
                    min-width: 15px;      
                    min-height: 30px;   
                }

                QScrollBar#scrollbar::handle:vertical:hover {
                    background: rgba(200, 200, 200, 0.5);
                }

                QScrollBar#scrollbar::groove:vertical {
                    border-radius: 10px;
                    width: 15px;
                }

                QScrollBar#scrollbar::add-line:vertical,
                QScrollBar#scrollbar::sub-line:vertical {
                    height: 0px;
                    background: none;
                }

                QScrollBar#scrollbar::add-page:vertical,
                QScrollBar#scrollbar::sub-page:vertical {
                    background: none;
                }

                #song_frame {
                    background-color: rgba(0, 0, 0, 0);
                }

                #song_content_frame {
                    margin-left: 15px;
                }

                #song_name {
                    border: none;
                    color: rgb(40, 40, 40);
                }

                #song_artist {
                    border: none;
                    color: rgb(0, 0, 0);
                }

                #more_button {
                    margin-left: 15px;
                    background-color: rgba(0, 0, 0, 0);
                }

            """
        )

