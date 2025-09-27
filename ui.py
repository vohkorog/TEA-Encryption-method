import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton


class Window(QWidget):
    
    

    def __init__(self):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.__line_edit = QLineEdit()
        self.__button = QPushButton("Отправить")
        
        self.__initField()
        self.__ui()

    def __initField(self):
        self.setWindowTitle("Window")
        self.resize(1000,500)
        self.setLayout(self.__layout)
        

        

    def __ui(self):
        self.__layout.addWidget(self.__line_edit)
        self.__layout.addWidget(self.__button)