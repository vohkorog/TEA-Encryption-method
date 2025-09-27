import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow
from SecondWIndow import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__centralWidget = QWidget()
        
        self.__layout = QVBoxLayout(self.__centralWidget)
        self.__line_edit = QLineEdit()
        self.__button = QPushButton("Отправить")
        self.__New_window_button = QPushButton("Открыть новое окно")
        self.__lable = QLabel("Привет,")

        self.__initField()
        self.__ui()
        self.__event()

    def __initField(self):
        self.setWindowTitle("Window")
        self.resize(1000,500)
        self.setCentralWidget(self.__centralWidget)
        self.setLayout(self.__layout)
        self.__line_edit.setPlaceholderText("Введите имя: ")

    def __ui(self):
        self.__layout.addWidget(self.__line_edit)
        self.__layout.addWidget(self.__lable)
        self.__layout.addWidget(self.__button)
        self.__layout.addWidget(self.__New_window_button)

    def __event(self):
        self.__button.clicked.connect(self.__onClickButton)
        self.__New_window_button.clicked.connect(self.__onClickNewWindowButton)

    def __onClickButton(self):
        self.__lable.setText(f"Привет, {self.__line_edit.text()}")

    def __onClickNewWindowButton(self):
        dialog = SecondWindow(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            pass