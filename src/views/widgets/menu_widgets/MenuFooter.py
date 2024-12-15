from PyQt5.QtWidgets import (
    QApplication, 
    QFrame, 
    QHBoxLayout, 
    QPushButton, 
    QLabel, 
    QWidget, 
    QVBoxLayout,
    QLineEdit,
    QGraphicsDropShadowEffect
)

from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt, QSize

from src.utils.helpers import center_widget

class MenuFooter(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        # Set geometry and layout for the footer
        self.setGeometry(25, 735, 500, 50)
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(100)

        # Add button
        self.add_button = QPushButton("Add")
        self.add_button.setFixedSize(80, 40)
        self.add_button.setIcon(QIcon("assets/icons/add_black.png"))
        self.add_button.setIconSize(QSize(20, 20))
        self.add_button.setObjectName("add_button")
        self.add_button.setCursor(Qt.PointingHandCursor)
        self.add_button.setFont(QFont("Itim", 12))
        self.add_button.clicked.connect(self.show_add_window)

        # Remove button
        self.remove_button = QPushButton("Remove")
        self.remove_button.setFixedSize(80, 40)
        self.remove_button.setIcon(QIcon("assets/icons/remove_black.png"))
        self.remove_button.setIconSize(QSize(20, 20))
        self.remove_button.setObjectName("remove_button")
        self.remove_button.setCursor(Qt.PointingHandCursor)
        self.remove_button.setFont(QFont("Itim", 12))

        # Navigation frame and buttons
        self.navigate_frame = QFrame(self)
        self.navigate_frame.setFixedSize(150, 40)

        # Next arrow button
        self.next_arrow_button = QPushButton(self.navigate_frame)
        self.next_arrow_button.setFixedSize(30, 30)
        self.next_arrow_button.setIcon(QIcon("assets/icons/next_arrow.png"))
        self.next_arrow_button.setIconSize(QSize(30, 30))
        self.next_arrow_button.setObjectName("next_arrow_button")
        self.next_arrow_button.setCursor(Qt.PointingHandCursor)

        # Back arrow button
        self.back_arrow_button = QPushButton(self.navigate_frame)
        self.back_arrow_button.setFixedSize(30, 30)
        self.back_arrow_button.setIcon(QIcon("assets/icons/back_arrow.png"))
        self.back_arrow_button.setIconSize(QSize(30, 30))
        self.back_arrow_button.setObjectName("back_arrow_button")
        self.back_arrow_button.setCursor(Qt.PointingHandCursor)

        # Navigation label
        self.navigate_label = QLabel(self.navigate_frame)
        self.navigate_label.setFixedSize(60, 30)
        self.navigate_label.setAlignment(Qt.AlignCenter)
        self.navigate_label.setObjectName("navigate_label")
        self.navigate_label.setText("1/1")
        self.navigate_label.setFont(QFont("Itim", 10))

        # Layout for navigation frame
        self.navigate_layout = QHBoxLayout(self.navigate_frame)
        self.navigate_layout.setAlignment(Qt.AlignCenter)
        self.navigate_layout.setContentsMargins(0, 0, 0, 0)
        self.navigate_layout.setSpacing(0)

        # Add navigation components to layout
        self.navigate_layout.addWidget(self.back_arrow_button)
        self.navigate_layout.addWidget(self.navigate_label)
        self.navigate_layout.addWidget(self.next_arrow_button)

        # Add widgets to the main layout
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.navigate_frame)
        self.layout.addWidget(self.remove_button)

        # create the pop up
        self.add_window = QWidget()
        self.add_window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.add_window.setAttribute(Qt.WA_TranslucentBackground, True)
        self.add_window.setObjectName("add_window")
        self.add_window.setFixedSize(300, 200)
        center_widget(self.add_window, QApplication.desktop().screenGeometry())

        self.add_window_layout = QVBoxLayout(self.add_window)
        self.add_window_layout.setSpacing(10)

        # create the background for the popup window
        self.popup_background = QFrame(self.add_window)
        self.popup_background.move(0, 0)
        self.popup_background.setFixedSize(300, 200)
        self.popup_background.setStyleSheet(
            """
                background: qlineargradient(
                        x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 rgb(200, 190, 230),
                        stop: 1 rgb(190, 120, 200)   
                    );

                border-radius: 20px;
            """
        )

        # creaate shadow effect for the pop up
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(10, 10)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.popup_background.setGraphicsEffect(shadow)

        # confirm label
        self.add_window_label = QLabel("Add song")
        self.add_window_label.setFont(QFont("Itim", 14))
        self.add_window_layout.addWidget(self.add_window_label)

        # song name input
        self.song_name_input = QLineEdit()
        self.song_name_input.setObjectName("song_name_input")
        self.song_name_input.setPlaceholderText("Song Name")
        self.song_name_input.setFont(QFont("Itim", 12))
        self.add_window_layout.addWidget(self.song_name_input)

        # artist name input
        self.artist_input = QLineEdit()
        self.artist_input.setObjectName("song_name_input")
        self.artist_input.setPlaceholderText("Artist Name")
        self.artist_input.setFont(QFont("Itim", 12))
        self.add_window_layout.addWidget(self.artist_input)

        # youtube link input
        self.link_input = QLineEdit()
        self.link_input.setObjectName("song_name_input")
        self.link_input.setPlaceholderText("YouTube Link")
        self.link_input.setFont(QFont("Itim", 12))
        self.add_window_layout.addWidget(self.link_input)

        # QFrame to contain the buttons
        self.buttons_frame = QFrame()
        self.buttons_frame.setFixedSize(275, 50)
        self.add_window_layout.addWidget(self.buttons_frame)

        # buttons container layout
        self.buttons_frame.layout = QHBoxLayout(self.buttons_frame)
        self.buttons_frame.layout.setAlignment(Qt.AlignCenter)
        self.buttons_frame.layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_frame.layout.setSpacing(110)

        # confirm button
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setObjectName("confirm_button")
        self.confirm_button.setFixedSize(80, 40)
        self.confirm_button.setIconSize(QSize(20, 20))
        self.confirm_button.setCursor(Qt.PointingHandCursor)
        self.confirm_button.setFont(QFont("Itim", 12))
        self.buttons_frame.layout.addWidget(self.confirm_button)

        # Cancel button
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setFixedSize(80, 40)
        self.cancel_button.setIconSize(QSize(20, 20))
        self.cancel_button.setCursor(Qt.PointingHandCursor)
        self.cancel_button.setFont(QFont("Itim", 12))
        self.cancel_button.clicked.connect(self.close_add_song_window)
        self.buttons_frame.layout.addWidget(self.cancel_button)

        self.add_window.hide() # set pop up hidden as default

        # styling the pop up window
        self.add_window.setStyleSheet(
            """
                #label {
                    color: black;
                    background-color: rgba(255, 255, 255, 0.5);
                }

                #song_name_input, #artist_input, #link_input {
                    border: none;
                    border-bottom: 1px solid black;
                    color: black;
                    background-color: transparent;
                }

                #confirm_button, #cancel_button {
                    padding-bottom: 5px;
                    border-radius: 15px;
                    color: black;
                    background-color: rgba(255, 255, 255, 0.4);
                }

                #confirm_button:hover, #cancel_button:hover {
                    background-color: rgba(255, 255, 255, 0.8);
                }
            """
        )

        # Set object name and styles
        self.setObjectName("menu_footer")
        self.setStyleSheet(
            """
                #add_button, #remove_button {
                    border-radius: 15px;
                    color: black;
                    background-color: rgba(255, 255, 255, 0.3);
                }
                #add_button:hover, #remove_button:hover {
                    background-color: rgba(255, 255, 255, 0.8);
                }
                #next_arrow_button, #back_arrow_button {
                    border-radius: 15px;
                    color: black;
                    background-color: transparent;
                }
                #navigate_label {
                    border-radius: 15px;
                    color: black;
                    background-color: rgba(255, 255, 255, 0.3);
                }
            """
        )

    def show_add_window(self):
        self.add_window.show()

    def close_add_song_window(self):
        self.add_window.close()


