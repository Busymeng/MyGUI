from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,600,400)
        self.setWindowTitle("Python GUI Development")
        self.setWindowIcon(QIcon("images\python-logo.png"))

        self.setStyleSheet("background-color:green")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())