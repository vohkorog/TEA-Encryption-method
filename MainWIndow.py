import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog, QScrollArea
from SecondWIndow import SecondWindow
from PyQt6.QtCore import pyqtSignal, Qt
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
        self.__New_window_button = QPushButton("Открыть новое окно")
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
        #self.__layout.addWidget(self.__New_window_button)
        self.__styleField()

    def __event(self):
        self.__button.clicked.connect(self.__onClickButton)
        #self.__New_window_button.clicked.connect(self.__onClickNewWindowButton)

    def __onClickButton(self):
        self.__plaintext = self.__line_edit.text()
        self.__lable.setText("=== Демонстрация TEA ===\n"
                             f"Исходный текст: {self.__plaintext}\n"
                             f"Длина исходного текста: {len(self.__plaintext)} байт\n")
        
        #self.encrypted = self.tea.encrypt_ecb(self.__plaintext)
        #self.decrypter = self.tea.decrypt_ecb(self.encrypted)



        

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
                max-height:100px;
                border-radius: 15px; 
            }
        """)

    def setText(self, number):

        self.__lable.setText("")
        self.__lable.setText(f"Привет, {self.name}, мне {str(number)} лет")

    def demo_tea():
    # Ключ 16 байт
    #key = b'16bytekey1234567'
    
    # Создаем шифратор
    #tea = TEACipher(key)
    
    # Текст для шифрования
    #plaintext = b'Hacking the Xbox: an introduction to reverse engineering'
    
        print("=== Демонстрация TEA ===")
        print(f"Исходный текст: {plaintext}")
        print(f"Длина исходного: {len(plaintext)} байт")
        
        # Шифрование ECB
        encrypted = tea.encrypt_ecb(plaintext)
        print(f"\nЗашифрованный (ECB): {encrypted.hex()}")
        print(f"Длина шифртекста: {len(encrypted)} байт")
        
        # Дешифрование ECB
        decrypted = tea.decrypt_ecb(encrypted)
        print(f"Расшифрованный (ECB): {decrypted}")
        
        # Демонстрация CBC режима
        print("\n=== Режим CBC ===")
        tea_adv = TEACipherAdvanced(key)
        iv = b'initvec!'  # 8 байт
        
        encrypted_cbc = tea_adv.encrypt_cbc(plaintext, iv)
        print(f"Зашифрованный (CBC): {encrypted_cbc.hex()}")
        
        decrypted_cbc = tea_adv.decrypt_cbc(encrypted_cbc, iv)
        print(f"Расшифрованный (CBC): {decrypted_cbc}")
        