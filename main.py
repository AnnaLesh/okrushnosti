import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# noinspection PyArgumentList
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.drawEllipse)
        self.f = False

    def drawEllipse(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            q = QPainter()
            q.begin(self)
            x, y = randint(50, 100), randint(50, 100)
            r = randint(20, 80)
            q.setBrush(QColor(255, 204, 0))
            q.drawEllipse(x, y, r, r)
            q.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
