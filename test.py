import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMainWindow, QDialog
from SecondWIndow import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Создаем центральный виджет
        self.__centralWidget = QWidget()
        
        # Создаем layout для центрального виджета
        self.__layout = QVBoxLayout(self.__centralWidget)  # Layout устанавливается здесь
        
        # Создаем виджеты
        self.__line_edit = QLineEdit()
        self.__button = QPushButton("Отправить")
        self.__New_window_button = QPushButton("Открыть новое окно")
        self.__lable = QLabel("Привет,")

        # Инициализация
        self.__initField()
        self.__ui()
        self.__event()

    def __initField(self):
        self.setWindowTitle("Window")
        self.resize(1000, 500)
        
        # Устанавливаем центральный виджет (layout уже установлен в конструкторе)
        self.setCentralWidget(self.__centralWidget)
        
        self.__line_edit.setPlaceholderText("Введите имя: ")

    def __ui(self):
        # Добавляем виджеты в layout
        self.__layout.addWidget(self.__line_edit)
        self.__layout.addWidget(self.__lable)
        self.__layout.addWidget(self.__button)
        self.__layout.addWidget(self.__New_window_button)
        
        # Применяем стили ПОСЛЕ добавления всех виджетов
        self.__styleField()

    def __event(self):
        self.__button.clicked.connect(self.__onClickButton)
        self.__New_window_button.clicked.connect(self.__onClickNewWindowButton)

    def __onClickButton(self):
        self.__lable.setText(f"Привет, {self.__line_edit.text()}")

    def __onClickNewWindowButton(self):
        dialog = SecondWindow(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            pass

    def __styleField(self):
        # Убедимся, что метка имеет достаточный размер для отображения фона
        self.__lable.setMinimumHeight(40)
        
        # Используем более конкретный стиль
        self.__lable.setStyleSheet("""
            QLabel {
                color: red; 
                background-color: yellow; 
                border: 2px solid black;
                padding: 10px;
                font-weight: bold;
            }
        """)
        
        # Принудительно обновляем отображение
        self.__lable.update()


# Добавьте это для тестирования, если SecondWindow недоступен
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Установим стиль приложения для лучшей совместимости
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())