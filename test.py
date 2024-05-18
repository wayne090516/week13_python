# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout

# app = QApplication(sys.argv)

# # 主窗口
# window = QWidget()
# window.setWindowTitle('Grid Layout Example')
# window.setGeometry(100, 100, 300, 200)

# # 主佈局
# layout = QGridLayout(window)

# # 創建 menu_widget 作為一個容器
# menu_widget = QWidget()
# menu_layout = QVBoxLayout(menu_widget)

# # 添加 6 個按鈕到 menu_layout
# for i in range(6):
#     button = QPushButton(f'Button {i + 1}')
#     menu_layout.addWidget(button)

# # 將 menu_widget 添加到主佈局
# layout.addWidget(menu_widget, 1, 0, 6, 1)

# window.setLayout(layout)
# window.show()

# sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea

class ScrollWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        main_layout = QVBoxLayout()

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        for i in range(20):
            label = QLabel(f"Label {i+1}", container_widget)
            container_layout.addWidget(label)

        scroll_area.setWidget(container_widget)

        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

        self.setWindowTitle('Scroll Area Example')
        self.setGeometry(300, 300, 300, 200)

def main():
    app = QApplication(sys.argv)
    window = ScrollWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
