from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, 
                             QWidget, QLineEdit, QPushButton, QLabel, QDialog, QHBoxLayout)
from PyQt6.QtCore import pyqtSignal
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("win")
        self.resize(400,300)
        self.centralWidget = QWidget()

        self.mylayout = QVBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)
        self.line_edit = QLineEdit()
        self.New_window_button = QPushButton("Открыть новое окно")

        self.mylayout.addWidget(self.line_edit)
        self.mylayout.addWidget(self.New_window_button)

        self.New_window_button.clicked.connect(self.onClick)

    def onClick(self):
        secondWin = SecWin(self)
        secondWin.dialog_signal.connect(self.on_number_received)
        secondWin.exec()

    def on_number_received(self, number):
        self.line_edit.setText(str(number))






class SecWin(QDialog):

    dialog_signal = pyqtSignal(object)

    def __init__(self, parent = None):
        super().__init__(parent)

        self.mylayout = QVBoxLayout()
        self.text_input = QLineEdit()
        self.buttonOK = QPushButton("OK")
        self.buttonCancel = QPushButton("Cancel")

        self.setWindowTitle('Ввод данных')
        self.resize(300,150)
        self.setLayout(self.mylayout)

        self.mylayout.addWidget(self.text_input)
        self.mylayout.addWidget(self.buttonOK)
        self.mylayout.addWidget(self.buttonCancel)

        self.buttonCancel.clicked.connect(self.close)
        self.buttonOK.clicked.connect(self.send_number)

    def send_number(self):
        
        number = self.text_input.text()
            # Отправляем сигнал с числом
        self.dialog_signal.emit(number)
        self.close()
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()