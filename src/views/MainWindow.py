from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import pyqtSignal, QTimer

# import from widgets
from src.views.widgets.background_widgets.Background import Background
from src.views.widgets.background_widgets.Title import Title

# import from containers
from src.views.containers.PlayerContainer import PlayerContainer
from src.views.containers.Menu import Menu

# import from helper
from src.utils.helpers import center_widget

class MainWindow(QMainWindow):
    
    # Signal to indicate that the main window has finished loading
    loading_complete = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.init_properties()
        self.init_children()        

        # emit the end signal
        QTimer.singleShot(3000, self.setup_complete)

    def init_properties(self):
        self.setWindowTitle("JukeBox")
        self.setMinimumSize(1115, 930)
        self.resize(1600, 1000)

        # center the window
        center_widget(self, QApplication.desktop().screenGeometry())

        # Set font for the application
        QFontDatabase.addApplicationFont("assets/fonts/Itim-Regular.ttf")
        

    def init_children(self):
        # Create background
        self.background = Background()
        self.setCentralWidget(self.background)

        # Title
        self.title = Title(self)

        # Song container frame
        self.player_container = PlayerContainer(self)

        # Menu frame
        self.menu_frame = Menu(self)

    def resizeEvent(self, event):
        """make the title and frames static"""

        # get window properties
        window_width = self.width()
        # window_height = self.height()
        middle_point = window_width // 2

        # Align the title
        self.title.setGeometry(0, 0, window_width, 150)  

        # Align the player frame
        player_frame_width = self.player_container.width()
        self.player_container.setGeometry(middle_point - player_frame_width + 1, 130 , 560, 800)
        
        # align the menu frame
        self.menu_frame.setGeometry(middle_point + 1, 130, 560, 800)

        # align pop ups
        width_change = (1600 - window_width) // 2
        self.menu_frame.search_bar.options_frame.setGeometry(1315 - width_change, 140, 120, 80)

    def setup_complete(self):
        """
        emit end signal when finished loading
        """
        self.loading_complete.emit()



