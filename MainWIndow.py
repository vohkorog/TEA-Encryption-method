import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt
from TEACipher import *

class MainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()

        self.key = b'16bytekey1234567'
        self.tea = TEACipher(self.key)

        self.__centralWidget = QWidget()
        
        self.__layout = QVBoxLayout(self.__centralWidget)
        self.__line_edit = QLineEdit()
        self.__button = QPushButton("Отправить")
        self.__lable = QLabel()       

        self.__initField()
        self.__ui()
        self.__event()

    def __initField(self):
        self.setWindowTitle("TEA encryption")
        self.resize(1000,400)
        self.setCentralWidget(self.__centralWidget)
        self.__line_edit.setPlaceholderText("Введите сообщение: ")
        self.__plaintext = ""

    def __ui(self):
        self.__layout.addWidget(self.__line_edit)
        self.__layout.addWidget(self.__lable)
        self.__layout.addWidget(self.__button)
        self.__styleField()

    def __event(self):
        self.__button.clicked.connect(self.__onClickButton)

    def __onClickButton(self):
        self.__plaintext = self.__line_edit.text()
        __plaintext_bytes = self.__plaintext.encode('utf-8')
        self.encrypted = self.tea.encrypt_ecb(__plaintext_bytes)
        self.__lable.setText("=== Демонстрация TEA ===\n"
                             f"Исходный текст: {self.__plaintext}\n"
                             f"Длина исходного текста: {len(self.__plaintext)} байт\n"
                             f"Зашифрованный (ECB): {self.encrypted.hex()}\n"
                             f"Длинна шифртекста: {len(self.encrypted)} байт\n")


    def __styleField(self):
        self.__lable.setStyleSheet("""
            QLabel {
                color: black; 
                background-color: #d6d0d0; 
                border: 2px solid black;
                padding: 10px;
                font-weight: bold;
                max-width:1000px ;
                max-height:300px;
                border-radius: 15px; 
            }
        """)

    def setText(self, number):

        self.__lable.setText("")
        self.__lable.setText(f"Привет, {self.name}, мне {str(number)} лет")