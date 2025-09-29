import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog, QDialogButtonBox
from PyQt6.QtCore import pyqtSignal

class SecondWindow(QDialog):

    signal = pyqtSignal(object)  # Сигнал для получения числа

    def __init__(self, parent=None):
        super().__init__(parent)      

        self.__layout = QVBoxLayout()
        self.__label = QLabel('Введите текст:')        
        self.__text_input = QLineEdit()
        self.__buttonOK = QPushButton("OK")
        self.__buttonCancel = QPushButton("Cancel")

        self.__initField()
        self.__ui()
        self.__event()


    def __initField(self):
        self.setWindowTitle('Ввод данных')
        self.resize(300,150)
        self.setLayout(self.__layout)


    def __ui(self):
        self.__layout.addWidget(self.__label)
        self.__layout.addWidget(self.__text_input)
        self.__layout.addWidget(self.__buttonOK)
        self.__layout.addWidget(self.__buttonCancel)
        
    def __event(self):
        self.__buttonCancel.clicked.connect(self.close)
        self.__buttonOK.clicked.connect(self.send_text)

    def send_text(self):
        text = self.__text_input.text()
        self.signal.emit(text)
        self.close()
     