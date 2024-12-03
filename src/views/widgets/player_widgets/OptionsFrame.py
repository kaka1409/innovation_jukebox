from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QStackedLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class OptionsFrame(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        # position the frame
        self.setGeometry(500, 25, 50, 280)

        # init layout for the frame
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(25)

        # contain all icon paths
        self.icon_paths = [
            "assets/icons/heart.png", # heart icon # 0
            "assets/icons/hearted.png", # hearted icon # 1
            "assets/icons/share.png", # share icon # 2
            "assets/icons/add.png", # add icon # 3
            "assets/icons/volume_off.png", # volume off icon # 4
            "assets/icons/volume_not_full.png", # volume not full icon # 5
            "assets/icons/volume_full", # full volume icon # 6
        ]

        # add icons to frame
        self.add_options()

        # stacked layout for volume buttons
        self.volume_frame = QFrame()
        self.volume_frame.setFixedSize(50, 50)
        self.volume_frame.stacked_layout = QStackedLayout(self.volume_frame)
        self.volume_change(80) # 80 is default volume value
        self.layout.insertWidget(3, self.volume_frame) # add to main layout

        # volume off icon
        self.volume_off_icon = QPushButton()
        self.volume_off_icon.setIcon(QIcon(self.icon_paths[4]))
        self.volume_off_icon.setIconSize(QSize(50, 50))
        self.volume_off_icon.setStyleSheet("padding-left: 7px;")
        self.volume_off_icon.setCursor(Qt.PointingHandCursor)
        self.volume_frame.stacked_layout.addWidget(self.volume_off_icon)

        # volume not full icon
        self.volume_not_full_icon = QPushButton()
        self.volume_not_full_icon.setIcon(QIcon(self.icon_paths[5]))
        self.volume_not_full_icon.setIconSize(QSize(50, 50))
        self.volume_not_full_icon.setStyleSheet("padding-left: 7px;")
        self.volume_not_full_icon.setCursor(Qt.PointingHandCursor)
        self.volume_frame.stacked_layout.addWidget(self.volume_not_full_icon)

        # volume full icon
        self.volume_full_icon = QPushButton()
        self.volume_full_icon.setIcon(QIcon(self.icon_paths[6]))
        self.volume_full_icon.setIconSize(QSize(50, 50))
        self.volume_full_icon.setStyleSheet("padding-left: 7px;")
        self.volume_full_icon.setCursor(Qt.PointingHandCursor)
        self.volume_frame.stacked_layout.addWidget(self.volume_full_icon)

        # set index 1 of the stacked volume button as default
        self.volume_frame.stacked_layout.setCurrentIndex(1)

        # heart icon
        heart_icon = self.layout.itemAt(0).widget()
        heart_icon.clicked.connect(lambda: self.hearted(heart_icon))

        self.is_hearted = False

        # styling
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

    def add_options(self):

        for index, icon_path in enumerate(self.icon_paths):
            # only add the first 3 icons

            # ignore hearted icon and volume icon
            if (index == 1 or
                index == 4 or 
                index == 5 or
                index ==  6) : 
                continue

            # create the button
            icon_btn = QPushButton()
            icon_btn.setFixedSize(50, 50)
            icon_btn.setIcon(QIcon(icon_path))
            
            # styling icons
            icon_btn.setIconSize(QSize(50, 50))
            icon_btn.setCursor(Qt.PointingHandCursor)
            icon_btn.setStyleSheet(
                """
                    QPushButton {
                        margin: 0;
                        padding: 0;
                        width: 50px;
                        height: 50px;
                        background-color: rgba(0, 0, 0, 0);
                        border-radius: 15px;
                        border: none;
                    }

                    QPushButton:hover {
                        background-color: rgba(255, 255, 255, 0.2)
                    }
                """
            )

            # add icon to layout
            self.layout.addWidget(icon_btn)

    def volume_change(self, value):
        """this function will be called whenver the volume changed"""
        
        if value in range(0, 1):
            self.volume_frame.stacked_layout.setCurrentIndex(0)

        if value in range(1, 99):
            self.volume_frame.stacked_layout.setCurrentIndex(1)

        if value == 100:
            self.volume_frame.stacked_layout.setCurrentIndex(2)

    def hearted(self, heart_icon):
        
        if self.is_hearted:

            heart_icon.setIcon(QIcon(self.icon_paths[0]))
            self.is_hearted = False

        else:

            heart_icon.setIcon(QIcon(self.icon_paths[1]))
            self.is_hearted = True



        



    