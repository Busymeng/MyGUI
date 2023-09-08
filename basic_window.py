
# Import necessary modules
import sys 
from PyQt6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):

    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        pass

# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())