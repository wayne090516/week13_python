from PyQt6 import QtWidgets, QtCore, QtGui


class LabelComponent(QtWidgets.QLabel):
    def __init__(self, font_size, content, style=""):
        super().__init__()

        self.setWordWrap(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.setFont(QtGui.QFont("微軟正黑體", font_size))
        self.setText(content)
        self.setStyleSheet(style)


class LineEditComponent(QtWidgets.QLineEdit):
    def __init__(self, default_content="", length=10, width=200, font_size=16):
        super().__init__()
        self.setMaxLength(length)
        self.setText(default_content)
        self.setMinimumHeight(30)
        self.setMaximumWidth(width)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))

    def clear_editor_content(self, event):
        self.clear()

    def disable(self):
        self.setEnabled(False)

    def enable(self):
        self.setEnabled(True)


class ButtonComponent(QtWidgets.QPushButton):
    def __init__(self, text, font_size=16):
        super().__init__()
        self.setText(text)
        self.setFont(QtGui.QFont("微軟正黑體", font_size))

    def disable(self):
        self.setEnabled(False)

    def enable(self):
        self.setEnabled(True)

class ScrollableLabelComponent(QtWidgets.QWidget):
    def __init__(self, font_size, content, style=""):
        super().__init__()

        self.label = LabelComponent(font_size, content, style)

        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.label)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(scroll_area)

        self.setLayout(layout)

    def set_text(self, text):
        self.label.setText(text)