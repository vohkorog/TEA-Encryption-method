import sys
from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow
from TEACipher import *

class MainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()

        self.name = ""  
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
        self.__lable.setText("=== Демонстрация TEA ===\n"
                             f"Исходный текст: {self.__plaintext}\n"
                             f"Длина исходного текста: {len(self.__plaintext)} байт\n")

        __plaintext_bytes = self.__plaintext.encode('utf-8')
        
        self.encrypted = self.tea.encrypt_ecb(__plaintext_bytes)
        #self.decrypter = self.tea.decrypt_ecb(self.encrypted)

    def __styleField(self):
        self.__lable.setStyleSheet("""
            QLabel {
                color: black; 
                background-color: #d6d0d0; 
                border: 2px solid black;
                padding: 10px;
                font-weight: bold;
                max-width:1000px ;
                max-height:100px;
                border-radius: 15px; 
            }
        """)
