import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Задача #2')

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('images/main.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    # Процедура решения примера
    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x >= 8:
                answer = ((x ** 2) / (a ** 2)) + ((x ** 2) / (b ** 2))
            else:
                answer = (x * ((a + b) ** 2))
            print(answer)
            self.label_answer.setText('Ответ: ' + format(answer, '.2f'))
        except:
            self.label_answer.setText('Ошибка!')

    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')


    # Основная часть программы
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()