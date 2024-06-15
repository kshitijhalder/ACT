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
        
import sys

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
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())