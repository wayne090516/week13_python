from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import QColor, QPalette, QFont
from PyQt6.QtWidgets import QStyle
import PyQt6.QtWidgets as QtWidgets

class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.setFont(QtGui.QFont("微軟正黑體", font_size))
        self.setText(content)


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16):
        super().__init__()
        self.setMaxLength(length)
        self.setPlaceholderText(default_content) 
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QFont("微軟正黑體", font_size))

        palette = QPalette(QColor("lightgray"))
        self.setPalette(palette)


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))
