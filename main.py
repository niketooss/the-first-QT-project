import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget


class Main(QWidget):
    def __init__(self):
        '''инициализация'''
        super().__init__()
        self.initUI()

    def initUI(self):
        '''Настройка интерфейса'''
        self.setGeometry(100, 100, 700, 700)
        self.setWindowTitle('Редактор текстовых файлов')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
