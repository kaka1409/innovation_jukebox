# import default packages
import sys
import time

# import packages from PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

# import important modules
from src.controllers.Controller import Controller
from src.views.LoadingScreen import LoadingScreen

# if __name__ == '__main__':

#         app = QApplication(sys.argv)
#         app.setWindowIcon(QIcon("assets/icons/window_icon.png")) # set window icon

#         initApp = Controller()

#         # show loading screen
#         loading_screen = LoadingScreen()
#         loading_screen.show()

#         # run main window
#         window = initApp.view_window
#         window.loading_complete.connect(loading_screen.close) # close loading screen
#         window.loading_complete.connect(window.show)

#         print(f"Starting time: {round(time.process_time(), 2)} seconds") # print the amount of time need to start the app
#         sys.exit(app.exec())


# no loading screen
if __name__ == '__main__':

        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon("assets/icons/window_icon.png")) # set window icon

        initApp = Controller()

        # run main window
        window = initApp.view_window
        window.show()

        print(f"Starting time: {round(time.process_time(), 2)} seconds") # print the amount of time need to start the app
        sys.exit(app.exec())
    