# Import necessary modules
import sys 
from PyQt6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):

    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        self.show()

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())
