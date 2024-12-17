from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QListWidgetItem,
    QGraphicsDropShadowEffect
)

from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt, QSize

from src.views.widgets.custom_widgets.CustomQFrame import CustomQFrame
from src.views.widgets.custom_widgets.CustomQListWidget import CustomQListWidget

class SearchBar(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.init_properties()
        self.init_children()
        self.init_appearance()
        
    def init_properties(self):

        # position
        self.setGeometry(30, 15, 475, 60)

        # layout
        self.layout = QHBoxLayout(self)

    def init_children(self):

        # search icon
        self.search_icon = QPushButton()
        self.search_icon.setFixedSize(30, 30)
        self.search_icon.setIcon(QIcon("assets/icons/search.png"))
        self.search_icon.setIconSize(QSize(20, 20))
        self.search_icon.setObjectName("search_icon")
        self.search_icon.setCursor(Qt.PointingHandCursor)
        self.layout.addWidget(self.search_icon) # add icon to search bar

        # search input line
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search")
        self.search_input.setFont(QFont("Itim", 8))
        self.search_input.setObjectName("search_input")
        self.layout.addWidget(self.search_input)
        self.search_input.textChanged.connect(self.on_searching)
        self.search_input.editingFinished.connect(self.end_searching)
        self.search_icon.show()

        # remove icon
        self.is_searching = False # remove_icon only show up when searching
        self.remove_icon = QPushButton(self.search_input)
        self.remove_icon.setFixedSize(20, 20)
        self.remove_icon.setIcon(QIcon("assets/icons/clear.png"))
        self.remove_icon.setGeometry(365, 2, 30, 30)
        self.remove_icon.setObjectName("remove_icon")
        self.remove_icon.setCursor(Qt.PointingHandCursor)
        self.remove_icon.hide() # hide as default

        # options icon
        self.options_icon = QPushButton()
        self.options_icon.setFixedSize(30, 30)
        self.options_icon.setIcon(QIcon("assets/icons/options.png"))
        self.options_icon.setIconSize(QSize(20, 20))
        self.options_icon.setObjectName("options_icon")
        self.options_icon.setCursor(Qt.PointingHandCursor)
        self.options_icon.clicked.connect(self.toggle_options_frame)
        self.layout.addWidget(self.options_icon) # add icon to search bar
        self.options_icon.show()

        # options frame
        main_window = self.parent().parent()
        self.options_frame = CustomQFrame()
        self.options_frame.setParent(main_window) # set the options frame is the children of the main window
        self.options_frame.setFixedSize(130, 80)
        self.options_frame.move(1315, 140)
        self.options_frame.setStyleSheet("border-radius: 15px; background-color: rgb(177, 156, 202);")
        self.options_frame.setVisible(False)

        # option list
        self.options_frame.options_list = CustomQListWidget()
        self.options_frame.options_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.options_frame.options_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.options_frame.options_list.setUniformItemSizes(True)
        self.options_frame.options_list.setFocusPolicy(Qt.NoFocus)
        self.options_frame.options_list.setCursor(Qt.PointingHandCursor)
        self.options_frame.options_list.setFixedSize(self.options_frame.size())

        # options state
        self.options_frame.options_list.is_searching_by_name = True # select search by name as default
        self.options_frame.options_list.is_searching_by_artist = False

        # shadow effect for the list widget
        list_shadow_effect = QGraphicsDropShadowEffect()
        list_shadow_effect.setBlurRadius(10)
        list_shadow_effect.setOffset(-5, 5)
        list_shadow_effect.setColor(QColor(50, 50, 50, 80)) # black color
        self.options_frame.setGraphicsEffect(list_shadow_effect)

        # create list items
        name_option_item = QListWidgetItem("Search by name")
        name_option_item.setFont(QFont("Itim", 10))
        name_option_item.setTextAlignment(Qt.AlignCenter)

        artist_option_item = QListWidgetItem("Search by artist")
        artist_option_item.setFont(QFont("Itim", 10))
        artist_option_item.setTextAlignment(Qt.AlignCenter)

        # add items to the list
        self.options_frame.options_list.addItem(name_option_item)
        self.options_frame.options_list.addItem(artist_option_item)

        # select the first item as default
        self.options_frame.options_list.setCurrentRow(0)

        # set layout for the options frame
        self.options_frame.layout = QVBoxLayout(self.options_frame)
        self.options_frame.layout.setAlignment(Qt.AlignCenter)
        self.options_frame.layout.setContentsMargins(0, 0, 0, 0)
        self.options_frame.layout.setSpacing(0)

        # add the list to the layout of the option frame
        self.options_frame.layout.addWidget(self.options_frame.options_list)

    def init_appearance(self):
        
        # styling the search bar
        self.setObjectName("search_container")
        self.setStyleSheet(
            """
                #search_container {
                    background-color: rgba(0, 0, 0, 0);
                    border-radius: 20px;
                    
                }

                #search_input {
                    max-width: 450px;
                    padding-top: 5px;
                    padding-bottom: 5px;
                    background-color: rgba(0, 0, 0, 0);
                    border: none;
                    border-bottom: 1px solid black;
                    font-size: 15px;
                }

                #search_icon {
                    margin: 0;
                    margin-bottom: 3px; 
                    padding: 0;
                    background-color: transparent;
                    max-width: 20px;
                    max-height: 20px;
                }

                #remove_icon {
                    margin-top: 5px;
                    background-color: transparent;
                    border: none;
                }

                #options_icon {
                    margin: 0;
                    margin-bottom: 3px;
                    padding: 0;
                    background-color: transparent;
                    margin-left: 5px;
                    max-width: 18px;
                    max-height: 18px;
                }

                #search_icon:hover, 
                #remove_icon:hover,
                #options_icon:hover {
                    background-color: rgba(255, 255, 255, 0.2)
                }

                #search_icon, 
                #remove_icon,
                #options_icon {
                    border-radius: 10px;
                }

            """
        )

        # styling the search options list
        self.options_frame.setStyleSheet(
            """
                QListWidget {
                    padding: 5px;
                    border-radius: 15px;
                    background: qlineargradient(
                        x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 rgb(200, 190, 230),
                        stop: 1 rgb(180, 170, 210)    
                    );
                }
                
                QListWidget::item {
                    margin: 2px 5px;
                    border-radius: 8px;
                    text-align: center;
                    height: 30px;
                }

                QListWidget::item:hover {
                    background-color: rgb(200, 200, 235); 
                }

                QListWidget::item:selected {
                    background-color: rgb(210, 210, 240);
                }
            """
        )

    def on_searching(self):
        """show remove icon when searching"""

        self.remove_icon.show()
        self.is_searching = True

    def end_searching(self):
        
        if self.get_search_input() == "":
            self.remove_icon.hide()
            self.is_searching = False

    def get_search_input(self):
        """return user input (remove whitespaces and lowercase)"""

        return str(self.search_input.text().replace(" ", "").lower())
    
    def toggle_options_frame(self):
        """select to search based song name or artist name"""

        # get current visibility state
        is_visible = self.options_frame.isVisible()

        # change visibility state
        self.options_frame.setVisible(not is_visible)
