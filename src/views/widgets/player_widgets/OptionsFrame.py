from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QStackedLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class OptionsFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.init_properties()
        self.init_children()
        self.init_appearance()

    def init_properties(self):
        # position the frame
        self.setGeometry(500, 25, 50, 280)

        # init layout for the frame
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(25)

    def init_children(self):

        # contain all icon paths
        self.icon_paths = {
            "heart": "assets/icons/heart.png", # heart icon # 0
            "hearted": "assets/icons/hearted.png", # hearted icon # 1
            "share": "assets/icons/share.png", # share icon # 2
            "add": "assets/icons/add.png", # add icon # 3
            "volume_off": "assets/icons/volume_off.png", # volume off icon # 4
            "volume_not_full": "assets/icons/volume_not_full.png", # volume not full icon # 5
            "volume_full": "assets/icons/volume_full", # full volume icon # 6
        }

        # creat all buttons for the layout
        self.heart_icon = QPushButton()                 # heart icon
        self.share_icon = QPushButton()                 # share icon
        self.add_icon = QPushButton()                   # add icon
        self.volume_off_icon = QPushButton()            # volume off icon
        self.volume_not_full_icon = QPushButton()       # volume not full icon
        self.volume_full_icon = QPushButton()           # volume full icon

        # stacked layout for volume buttons
        self.volume_frame = QFrame()
        self.volume_frame.setFixedSize(50, 50)
        self.volume_frame.stacked_layout = QStackedLayout(self.volume_frame)
        
        # style all buttons
        self.init_button_properties(
            {
                "heart": self.heart_icon,               
                "share": self.share_icon,               
                "add": self.add_icon,                 
                "volume_off": self.volume_off_icon,           
                "volume_not_full": self.volume_not_full_icon,       
                "volume_full": self.volume_full_icon, 
            }
        )

        self.layout.insertWidget(3, self.volume_frame) # add to main layout

        # default 
        self.volume_frame.stacked_layout.setCurrentIndex(1) # set index 1 of the stacked volume button as default
        self.volume_change(60) # 60 is default volume value

        # heart icon event connection
        self.heart_icon.clicked.connect(self.hearted)

        self.is_hearted = False

    def init_button_properties(self, button_dictionary):
        """
        change appearance of buttons in the options bar
        """

        for button_key in button_dictionary:
            
            # get button widget from the key in dictionary
            button = button_dictionary[button_key]

            # set button properties
            button.setIcon(QIcon(self.icon_paths[button_key]))
            button.setIconSize(QSize(50, 50))
            button.setCursor(Qt.PointingHandCursor)

            # volume button will be addded extra left padding
            if "volume" in button_key: button.setStyleSheet("padding-left: 7px;")

            # add to suitable layout
            # if is not a volume button will be added to main layout
            # else is a volume button will be added to volume stacked layout
            main_layout = self.layout
            stacked_volume_layout = self.volume_frame.stacked_layout

            if not "volume" in button_key:
                main_layout.addWidget(button)
            else:
                stacked_volume_layout.addWidget(button)

    def init_appearance(self):

        self.setObjectName("options_frame")
        self.setStyleSheet(
            """
                #options_frame {
                    margin: 0;
                    padding: 0;
                }

                QPushButton {
                    border-radius: 15px;
                    background-color: rgba(0, 0, 0, 0);
                    border: none;
                }

                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.2)
                }
            """
        )

    """
    Any methods below styling will be specific functions that have role to update the UI
    """

    def volume_change(self, value):
        """
        this function will be called whenver the volume changed
        """
        
        index = 1 # default index

        if value in range(0, 1): index = 0
        if value in range(1, 99): index = 1
        if value in range(99, 100): index = 2

        self.volume_frame.stacked_layout.setCurrentIndex(index)

    def hearted(self):
        """
        Toggle the heart button icon when clicked, and change the
        state of self.is_hearted accordingly.
        """

        # heart icons
        heart_icon = self.icon_paths["heart"]
        hearted_icon = self.icon_paths["hearted"]

        if self.is_hearted == False:
            self.heart_icon.setIcon(QIcon(heart_icon))
            self.is_hearted = True
        else:
            self.heart_icon.setIcon(QIcon(hearted_icon))
            self.is_hearted = False




        



    