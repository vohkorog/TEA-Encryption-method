import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog, QScrollArea
from PyQt6.QtCore import pyqtSignal, Qt
from TEACipher import *

class MainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()
        
        self.__plaintext = ""
        #self.key = b'16bytekey1234567'
        #self.tea = TEACipher(self.key)

        self.__centralWidget = QWidget()
        self.__mainLayout = QVBoxLayout(self.__centralWidget)
        self.__textLayout = QHBoxLayout()
        self.__buttonLayout = QHBoxLayout()
        

        self.__line_edit = QLineEdit()
        self.__key_line_edit = QLineEdit()
        self.__buttonEncrypted = QPushButton("Зашифровать")
        self.__buttonDecrypted = QPushButton("Расшифровать")
        self.__text_left = QTextEdit()
        self.__text_right = QTextEdit()
        

        self.__initField()
        self.__ui()
        self.__event()

    def __initField(self):
        self.setWindowTitle("TEA encryption")
        self.resize(1000,400)
        self.setCentralWidget(self.__centralWidget)
        
        self.__line_edit.setPlaceholderText("Введите сообщение: ")
        self.__key_line_edit.setPlaceholderText("Введите ключ: ")
        
        self.__text_left.setReadOnly(True)
        self.__text_left.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.__text_left.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.__text_left.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse |
            Qt.TextInteractionFlag.TextSelectableByKeyboard
        )

        self.__text_right.setReadOnly(True)
        self.__text_right.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.__text_right.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.__text_right.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse |
            Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
    
    
    def __ui(self):
        self.__mainLayout.addWidget(self.__line_edit)
        self.__mainLayout.addWidget(self.__key_line_edit)

        self.__textLayout.addWidget(self.__text_left)
        self.__textLayout.addWidget(self.__text_right)

        self.__buttonLayout.addWidget(self.__buttonEncrypted)
        self.__buttonLayout.addWidget(self.__buttonDecrypted)

        self.__mainLayout.addLayout(self.__textLayout)
        self.__mainLayout.addLayout(self.__buttonLayout)

        self.__styleField()

    def __event(self):
        self.__buttonEncrypted.clicked.connect(self.__onClickButtonEncrypted)
        self.__buttonDecrypted.clicked.connect(self.__onClickButtonDecrypted)

    def __onClickButtonEncrypted(self):

        self.key = self.__key_line_edit.text()
        __keytext_bytes = self.key.encode('utf-8')
        tea = TEACipher(__keytext_bytes)
        
        self.__plaintext = self.__line_edit.text()
        __plaintext_bytes = self.__plaintext.encode('utf-8')
        encrypted = tea.encrypt_ecb(__plaintext_bytes)
        self.__text_left.setText("=== Демонстрация TEA ===\n"
                             f"Исходный текст: {self.__plaintext}\n"
                             f"Длина исходного текста: {len(self.__plaintext)} байт\n"
                             f"Зашифрованный (ECB): {encrypted.hex()}\n"
                             f"Длинна шифртекста: {len(encrypted)} байт\n")


    def __onClickButtonDecrypted(self):

        self.key = self.__key_line_edit.text()
        __keytext_bytes = self.key.encode('utf-8')
        tea = TEACipher(__keytext_bytes)

        __plaintext = self.__line_edit.text()
        result = tea.decrypt_ecb_hex(__plaintext)

        self.__text_right.setText(f"Расшифрованный (ECB): {result}\n")



    def __styleField(self):
     #   self.__lable.setStyleSheet("""
      #      QLabel {
       #         color: black; 
        #        background-color: #d6d0d0; 
         #       border: 2px solid black;
          #      padding: 10px;
           #     font-weight: bold;
            #    max-width:1000px ;
             #   max-height:300px;
              #  border-radius: 15px; 
           # }
       # """)
       pass