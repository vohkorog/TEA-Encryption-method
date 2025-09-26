import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton


class Window(QWidget):
    
    
    def __init__(self):
        super().__init__()
        self.__initField()

    def __initField(self):
        self.setWindowTitle("Window")
        self.resize(1000,500)

    
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
    