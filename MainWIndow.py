
from PyQt6.QtWidgets import QWidget, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from TEACipher import *

class MainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()
        
        self.__plaintext = ""

        self.__centralWidget = QWidget()
        self.__mainLayout = QVBoxLayout(self.__centralWidget)
        self.__textLayout = QHBoxLayout()
        self.__buttonLayout = QHBoxLayout()
        
    
        self.__count_word = QLabel()
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
        self.__key_line_edit.textChanged.connect(self.update_counter)

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
        self.__mainLayout.addWidget(self.__count_word)

        self.__textLayout.addWidget(self.__text_left)
        self.__textLayout.addWidget(self.__text_right)

        self.__buttonLayout.addWidget(self.__buttonEncrypted)
        self.__buttonLayout.addWidget(self.__buttonDecrypted)

        self.__mainLayout.addLayout(self.__textLayout)
        self.__mainLayout.addLayout(self.__buttonLayout)

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

    def update_counter(self):
        text = self.__key_line_edit.text()
        count = len(text)
        self.__count_word.setText(f'Символов в ключе: {count}')




    