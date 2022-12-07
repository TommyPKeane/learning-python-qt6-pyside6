import sys

from PySide6 import QtWidgets

from custom_widgets.simple_window import SimpleWindow


if __name__ == "__main__":
    qt_app = QtWidgets.QApplication([])

    window_width = 800
    window_height = 600

    widget = SimpleWindow()
    widget.resize(window_width, window_height)
    widget.show()

    sys.exit(qt_app.exec())
