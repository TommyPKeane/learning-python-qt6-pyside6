"""Example Simple Window Widget

References:
- https://doc.qt.io/qtforpython/quickstart.html
"""
import random

from PySide6 import (
    QtCore,
    QtWidgets,
    QtGui,
)


class SimpleWindow(QtWidgets.QWidget):
    """Simple Window Widget

    Attributes:
        button (QtWidgets.QPushButton): ...
        hello (list[str]): ...
        layout (QtWidgets.QVBoxLayout): ...
        text (QtWidgets.QLabel): ...
    """

    _current_text = None
    _new_text = None

    def __init__(self):
        super().__init__()
        self.hello = [
            "🇺🇸 Hello World",
            "🇩🇪 Hallo Welt",
            "🇫🇮 Hei maailma",
            "🇪🇸 Hola Mundo",
            "🇷🇺 Привет мир",
        ]
        self._current_text = self.hello[0]
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(
            self._current_text,
            alignment=QtCore.Qt.AlignCenter,
        )
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.update_greeting)
        return None

    @QtCore.Slot()
    def update_greeting(self):
        """(Callback | Slot) Update the Greeting in the Window

        This method relies on Python's `random.choice()`, but there's a risk
        that the random value will be the same as the current value, so there is
        extra logic introduced here to ensure that the greeting will always be
        updated to a new value.

        Returns:
            None: Nothing returned
        """
        random_hello = random.choice(self.hello)
        _current_index = self.hello.index(self._current_text)
        _fallback_new_index = ((_current_index + 1) % len(self.hello))
        self._new_text = (
            random_hello
            if random_hello != self._current_text
            else self.hello[_fallback_new_index]
        )
        self.text.setText(self._new_text)
        self._current_text = self._new_text
        return None
