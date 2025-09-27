import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog, QDialogButtonBox

class SecondWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Ввод данных')
        self.setGeometry(250, 250, 300, 150)
        
        layout = QVBoxLayout()
        
        self.label = QLabel('Введите текст:')
        layout.addWidget(self.label)
        
        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)
        
        # Кнопки OK и Cancel
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.setLayout(layout)
    
    def get_text(self):
        return self.text_input.text()