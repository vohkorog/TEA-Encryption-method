import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel


class Window(QWidget):
    
    

    def __init__(self):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.__line_edit = QLineEdit()
        self.__button = QPushButton("Отправить")
        self.__lable = QLabel("Привет,")

        self.__initField()
        self.__ui()
        self.__event()

    def __initField(self):
        self.setWindowTitle("Window")
        self.resize(1000,500)
        self.setLayout(self.__layout)
        self.__line_edit.setPlaceholderText("Введите имя: ")
        
    

    def __onClick(self):
        self.__lable.setText(f"Привет, {self.__line_edit.text()}")

    def __ui(self):
        self.__layout.addWidget(self.__line_edit)
        self.__layout.addWidget(self.__lable)
        self.__layout.addWidget(self.__button)

    def __event(self):
        self.__button.clicked.connect(self.__onClick)