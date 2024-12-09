from PyQt5.QtWidgets import (
    QVBoxLayout,
    QFrame,
    QLabel,
    QGraphicsScene,
    QGraphicsProxyWidget,
)

from PyQt5.QtGui import QPixmap, QPainterPath, QRegion
from PyQt5.QtCore import Qt, QPropertyAnimation

from src.views.widgets.custom_widgets.CustomGraphicView import CustomGraphicsView

class Thumbnail(QFrame):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.init_properties()
        self.init_children()
        self.init_thumbnail_animation()

    def init_properties(self):
        # Set the geometry and size of the thumbnail frame
        self.setGeometry(130, 180, 300, 300)
        self.setStyleSheet("background-color: transparent; border-radius: 300px;")

        # Set layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

    def init_children(self):
        # Default image path
        default_image_path = "assets/images/song_thumbnails/A_New_Kind_Of_Love.jpg"

        # Create a QGraphicsView and QGraphicsScene
        self.view = CustomGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setStyleSheet("background: transparent; border-radius: 300px;")
        self.layout.addWidget(self.view)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 300, 300) # lock sceen size
        self.view.setScene(self.scene)

        # Create a QFrame and embed it in a QGraphicsProxyWidget
        self.proxy_frame = QFrame()
        self.proxy_frame.setFixedSize(300, 300)
        self.proxy_frame.setStyleSheet("background-color: transparent; border-radius: 300px;")

        self.proxy_widget = QGraphicsProxyWidget()
        self.proxy_widget.setWidget(self.proxy_frame)
        self.proxy_widget.setTransformOriginPoint(150, 150)  # Rotate around the center (150,150 is half of Qframe dimension)
        self.scene.addItem(self.proxy_widget)

        # Create the QLabel inside the proxy frame
        self.image = QLabel(self.proxy_frame)
        self.image.setStyleSheet("border-radius: 300px;")
        self.image.setGeometry(0, 0, 300, 300)
        self.image.setAlignment(Qt.AlignCenter)

        # Create a rounded path for masking
        path = QPainterPath()
        corner_radius = 300  # Adjust corner radius for smoother corners
        path.addRoundedRect(0, 0, 300, 300, corner_radius, corner_radius)

        # Apply the rounded mask to the QLabel
        region = QRegion(path.toFillPolygon().toPolygon())
        self.image.setMask(region)

        # Load and set the default pixmap
        pixmap = QPixmap(default_image_path).scaled(
            300,
            300,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation,
        )
        
        self.image.setPixmap(pixmap)

        # display the thumbnail
        self.image.show()

    def init_thumbnail_animation(self):
        # Rotate animation
        self.rotate_animation = QPropertyAnimation(self.proxy_widget, b"rotation")
        self.rotate_animation.setDuration(5000)  # Duration for a full rotation (2000ms)
        self.rotate_animation.setStartValue(0)  # Start angle
        self.rotate_animation.setEndValue(360)  # End angle
        self.rotate_animation.setLoopCount(-1)  # Infinite loop

        # Animation state
        self.is_rotating = False
        self.current_angle = 0

    def change_thumbnail(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():  # Check if the new image is valid
            pixmap = pixmap.scaled(
                self.width(),
                self.height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation,
            )
            self.image.setPixmap(pixmap)
        else:
            self.image.setText("Image not found!")
            self.image.setStyleSheet("color: white; font-size: 30px;")

    def start_rotating(self):

        self.rotate_animation.setStartValue(self.current_angle)
        self.rotate_animation.setEndValue(self.current_angle + 360)  # Full rotation
        self.rotate_animation.start()
        self.is_rotating = True

    def pause_rotating(self):

        self.rotate_animation.stop()
        self.current_angle = self.proxy_widget.rotation() % 360  # Store the rotation
        self.is_rotating = False

    def reset_animation(self):
        
        self.current_angle = 0
        self.is_rotating = False

        self.rotate_animation.setStartValue(0)
        self.rotate_animation.start()
        self.rotate_animation.stop()
        self.rotate_animation.setStartValue(360)
