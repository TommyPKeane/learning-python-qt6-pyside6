"""Example with Canvas

References:
- https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/
- https://www.pythonguis.com/faq/resizing-the-qpainter-canvas/
"""
import random
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()
        return None

    def resizeEvent(self, event):
        new_size = event.size()
        canvas = QtGui.QPixmap(new_size.width(), new_size.height())
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.draw_something()
        return super(QtWidgets.QMainWindow, self).resizeEvent(event)

    def draw_something(self):
        colors = ["#FFD141", "#376F9F", "#0D1F2D", "#E9EBEF", "#EB5160"]
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        for n in range(10000):
            # pen = painter.pen() you could get the active pen here
            pen.setColor(QtGui.QColor(random.choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                (self.width() // 2)+random.randint(-100, 100),  # x
                (self.height() // 2)+random.randint(-100, 100)   # y
                )
        painter.end()
        self.label.setPixmap(canvas)
        return None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_width = 400
    window_height = 300
    window = MainWindow()
    window.resize(window_width, window_height)
    window.show()
    sys.exit(app.exec())
