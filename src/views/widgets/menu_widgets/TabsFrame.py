from PyQt5.QtWidgets import QPushButton, QFrame, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QPoint

class TabsFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setGeometry(25, 70, 488, 60)

        # init layout of the frame 
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(30)

        # specific attribute to store tabs and selected tab
        self.tab_buttons = [] # store all tabs button
        self.selected_tab = None  # selected button
        self.selected_tab_index = 0 # index of selected tab = 0 as default 
        # selected_tab_index is cruial to menu's QStackedLayout

        # line
        self.indicator = QFrame(self)
        self.indicator.setStyleSheet("background-color: black;")
        self.indicator.setFixedHeight(2)  
        self.indicator.setGeometry(12, 45, 50, 2)  
        
        self.renderTabs()  # Initialize all tabs

        self.setLayout(self.layout)  # Set layout

        self.setObjectName("tabs_frame")
        self.setStyleSheet(
            """
                #tabs_frame {
                    padding: 0;
                    margin: 0;
                }
            """
        )

    def renderTabs(self):
        tabs = ["Song", "Playlist", "Favorite", "Genre", "Artist"]

        for index, tab in enumerate(tabs):

            # create the button
            tab_btn = QPushButton(tab)
            tab_btn.setFont(QFont("Itim", 14, QFont.Light))
            tab_btn.setCursor(Qt.PointingHandCursor)
            tab_btn.setStyleSheet(
                """
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

            # append the index to the button object
            tab_btn.tab_index = index

            # set song tab is selected as default
            if tab == "Song": 
                self.selected_tab = tab_btn
                self.selected_tab.setFont(QFont("Itim", 14, QFont.Bold))

            # Add button to layout
            self.layout.addWidget(tab_btn)
            self.tab_buttons.append(tab_btn)

            # click event
            tab_btn.clicked.connect(lambda _, btn = tab_btn: self.select_tab(btn))

    def select_tab(self, selected_tab):

        # Reset the previous tab
        if self.selected_tab is not None:
            self.selected_tab.setFont(QFont("Itim", 14, QFont.Light))

        # Update the font of the currently selected button
        selected_tab.setFont(QFont("Itim", 14, QFont.Bold))

        # set the currently selected button
        self.selected_tab = selected_tab
        self.selected_tab_index = selected_tab.tab_index

        # move indicator under the selected tab
        self.move_indicator(selected_tab)

    def move_indicator(self, selected_tab):
        """Move the line under the selected tab"""

        # get text width
        text_width = self.get_text_width(self.selected_tab)
        line_padding = self.get_line_padding(self.selected_tab)

        # Get global position of the tab
        tab_pos = selected_tab.mapToParent(QPoint(0, 0))

        # moving animation
        self.moving_line_animation = QPropertyAnimation(self.indicator, b"geometry")
        self.moving_line_animation.setDuration(150)  #  duration

        # Set start and end values for the animation
        start_value = self.indicator.geometry()
        end_value = QRect(tab_pos.x() + line_padding, 45, text_width, 2)

        self.moving_line_animation.setStartValue(start_value)
        self.moving_line_animation.setEndValue(end_value)

        self.moving_line_animation.start()
        
    def get_text_width(self, button):
        """return the width of the text in the button"""
        return button.fontMetrics().boundingRect(button.text()).width()
    
    def get_line_padding(self, button):
        """return padding to make the line align correctly with the tab"""

        text_width = self.get_text_width(button)
        return (button.width() - text_width) // 2
    
    def get_selected_tab(self):
        """get the index of the selected tab"""

        return self.selected_tab_index



