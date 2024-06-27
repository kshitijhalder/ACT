# Learning PySide6
# Date: 2024-06-17
# Source: https://www.youtube.com/watch?v=Z1N9JzNax2k&list=WL&index=3&t=1142s

# Import necessary modules
from PySide6 import QtWidgets
import sys

# Create a new instance of the QApplication class. This is required for any GUI application.
app = QApplication(sys.argv)

# Create a new instance of the QWidget class to create a window.
window = QWidget()

# Display the window on the screen.
window.show()

# Start the main event loop, where the application will start processing events and interacting with the user.
app.exec_()