import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog
from SecondWIndow import SecondWindow
from PyQt6.QtCore import pyqtSignal


class MainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()

        self.name = ""    
        self.__centralWidget = QWidget()
        
        self.__layout = QVBoxLayout(self.__centralWidget)
        self.__line_edit = QLineEdit()
        self.__button = QPushButton("Отправить")
        self.__New_window_button = QPushButton("Открыть новое окно")
        self.__lable = QLabel()

        self.__initField()
        self.__ui()
        self.__event()

    def __initField(self):
        self.setWindowTitle("Window")
        self.resize(1000,200)
        self.setCentralWidget(self.__centralWidget)
        self.__line_edit.setPlaceholderText("Введите имя: ")

    def __ui(self):
        self.__layout.addWidget(self.__line_edit)
        self.__layout.addWidget(self.__lable)
        self.__layout.addWidget(self.__button)
        self.__layout.addWidget(self.__New_window_button)
        self.__styleField()

    def __event(self):
        self.__button.clicked.connect(self.__onClickButton)
        self.__New_window_button.clicked.connect(self.__onClickNewWindowButton)

    def __onClickButton(self):
        self.hello = "Привет,"
        self.__lable.setText("")
        self.name = self.__line_edit.text()
        self.__lable.setText(f"{self.hello} {self.name}")

    def __onClickNewWindowButton(self):
        dialog = SecondWindow(self)
        dialog.signal.connect(self.setText)
        dialog.exec()

    def __styleField(self):
        self.__lable.setStyleSheet("""
            QLabel {
                color: black; 
                background-color: #d6d0d0; 
                border: 2px solid black;
                padding: 10px;
                font-weight: bold;
                max-width:1000px ;
                max-height:30px;
                border-radius: 15px; 
            }
        """)

    def setText(self, number):

        self.__lable.setText("")
        self.__lable.setText(f"Привет, {self.name}, мне {str(number)} лет")
        