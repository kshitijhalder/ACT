from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from getpass import getpass
import sys

class PyToggle(QCheckBox):
    def __init__(self, width=60, bg_color="#777", circle_color="#DDD", active_color="#00BCff"):
        super().__init__()
        
        self.width = width
        self.bg_color = bg_color
        self.circle_color = circle_color
        self.active_color = active_color

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        if not isinstance(width, int) or width <= 0:
            print("Invalid width specified. Using default value of 60.")
            width = 60
        self.width = width
        
        self.resize(500, 500)

        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color: #222 }")
        self.layout = QVBoxLayout()

        self.toggle = PyToggle()
        self.layout.addWidget(self.toggle)
        self.layout.setAlignment(Qt.AlignCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        if not isinstance(bg_color, str):
            print("Invalid background color specified. Using default value of #777.")
            bg_color = "#777"
        self.bg_color = bg_color
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())




"""
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from getpass import getpass

class PyToggle(QCheckBox):
    def __init__(
        self,
        width = 60,
        bg_color = "#777",
        circle_color = "#DDD",
        active_color = "#00BCff",
    ):
        QCheckBox.__init__(self)
        if not isinstance(circle_color, str):
            print("Invalid circle color specified. Using default value of #DDD.")
            circle_color = "#DDD"
        self.circle_color = circle_color
        
import sys

        if not isinstance(active_color, str):
            print("Invalid active color specified. Using default value of #00BCff.")
            active_color = "#00BCff"
        self.active_color = active_color
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # RESIZE WINDOW
        self.resize (500, 500)

        # CREATE CONTAINER AND LAYOUT
        self.container = QFrame()
        self.container.setObjectName ("container")
        self.container.setStyleSheet ("#container { background-color: #222 }")
        self.layout = QVBoxLayout()
    
        # ADD WIDGETS TO LAYOUT
        self.toggle = PyToggle()
    
        self.layout.addwidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)
        
        # SET CENTRAL WIDGET
        self.container.setLayout (self.layout)
        self.setCentralWidget(self.container)
        
        # SHOW WINDOW
        try:
            self.resize(500, 500)
        except Exception as e:
            print(f"Error resizing window: {str(e)}")
            return
        
        try:
            self.container = QFrame()
            self.container.setObjectName("container")
            self.container.setStyleSheet("#container { background-color: #222 }")
            self.layout = QVBoxLayout()

            try:
                self.toggle = PyToggle()
                self.layout.addWidget(self.toggle)
                self.layout.setAlignment(Qt.AlignCenter)

                self.container.setLayout(self.layout)
                self.setCentralWidget(self.container)
        self.show()
            except Exception as e:
                print(f"Error creating GUI: {str(e)}")
        except Exception as e:
            print(f"Error initializing window: {str(e)}")

if __name__ == "__main__":
    try:
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
"""
    