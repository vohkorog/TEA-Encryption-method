import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog, QDialogButtonBox

class SecondWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)      

        self.__layout = QVBoxLayout()
        self.__label = QLabel('Введите текст:')        
        self.__text_input = QLineEdit()
        self.__buttonOK = QPushButton("OK")
        self.__buttonCancel = QPushButton("Cancel")
        
       # buttons.accepted.connect(self.accept)
       # buttons.rejected.connect(self.reject)

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

    def get_text(self):
        return self.text_input.text()