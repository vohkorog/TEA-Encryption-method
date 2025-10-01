import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLineEdit, QTextEdit, QPushButton, QStatusBar)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollable Text Layout - QMainWindow")
        self.setGeometry(100, 100, 800, 600)
        
        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # 1. QLineEdit сверху
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите текст здесь...")
        self.line_edit.setStyleSheet("padding: 8px; font-size: 14px;")
        main_layout.addWidget(self.line_edit)
        
        # 2. Два QTextEdit с скроллбарами посередине
        text_layout = QHBoxLayout()
        
        # Левый текстовый виджет
        self.text_left = self.create_readonly_textedit()
        self.text_left.setPlainText("Это левая текстовая область.\nМожно прокручивать\nи копировать текст,\nно нельзя редактировать." * 5)
        
        # Правый текстовый виджет
        self.text_right = self.create_readonly_textedit()
        self.text_right.setPlainText("Это правая текстовая область.\nТоже с скроллбаром\nи возможностью копирования." * 5)
        
        text_layout.addWidget(self.text_left)
        text_layout.addWidget(self.text_right)
        
        main_layout.addLayout(text_layout)
        
        # 3. Две кнопки внизу
        buttons_layout = QHBoxLayout()
        
        self.button1 = QPushButton("Обновить левый текст")
        self.button2 = QPushButton("Обновить правый текст")
        
        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)
        
        main_layout.addLayout(buttons_layout)
        
        # Настройка растяжения
        main_layout.setStretch(1, 1)  # Текстовые области растягиваются
        
        central_widget.setLayout(main_layout)
        
        # Добавляем статус бар (преимущество QMainWindow)
        self.statusBar().showMessage("Готов к работе")
        
        # Подключаем сигналы
        self.connect_signals()
    
    def create_readonly_textedit(self):
        """Создает QTextEdit в режиме только для чтения со скроллбаром"""
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        text_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        text_edit.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse |
            Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
        
        text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
        """)
        
        return text_edit
    
    def connect_signals(self):
        """Подключение сигналов"""
        self.line_edit.returnPressed.connect(self.on_enter_pressed)
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        
        # Сигналы для выделения текста
        self.text_left.selectionChanged.connect(self.on_text_selected)
        self.text_right.selectionChanged.connect(self.on_text_selected)
    
    def on_enter_pressed(self):
        """При нажатии Enter добавляем текст в левую область"""
        text = self.line_edit.text()
        if text:
            current_text = self.text_left.toPlainText()
            self.text_left.setPlainText(current_text + f"\n> {text}")
            self.line_edit.clear()
            self.text_left.verticalScrollBar().setValue(
                self.text_left.verticalScrollBar().maximum()
            )
            self.statusBar().showMessage("Текст добавлен в левую область")
    
    def on_button1_clicked(self):
        """Обновляет левый текст"""
        self.text_left.setPlainText("Левый текст обновлен!\n" + 
                                  "Можно выделить этот текст\nи скопировать его (Ctrl+C).\n" * 3)
        self.statusBar().showMessage("Левый текст обновлен")
    
    def on_button2_clicked(self):
        """Обновляет правый текст"""
        self.text_right.setPlainText("Правый текст обновлен!\n" +
                                   "Попробуйте выделить текст\nи нажать Ctrl+C - он скопируется!\n" * 3)
        self.statusBar().showMessage("Правый текст обновлен")
    
    def on_text_selected(self):
        """Показывает сообщение при выделении текста"""
        self.statusBar().showMessage("Текст выделен - можно копировать (Ctrl+C)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())