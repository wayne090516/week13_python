from PyQt6 import QtWidgets
from WorkWidgets.WidgetComponents import LabelComponent
from client.ServiceController import ExecuteCommand
import json


class ShowStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("show_stu_widget")

        layout = QtWidgets.QGridLayout()

        header_label = LabelComponent(20, "Show Student")

        self.container_widget = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)

        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.container_widget)

        layout.addWidget(header_label, 0, 0)
        layout.addWidget(self.scroll_area, 1, 0)

        # Set Layout
        layout.setColumnStretch(0, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 6)

        self.setLayout(layout)

    def load(self):
        print("show widget")
        self.execute_show = ExecuteCommand(command="show", data={})
        self.execute_show.start()
        self.execute_show.return_sig.connect(self.show_action_result)

    def show_action_result(self, result):
        result = eval(json.loads(result))
        student_dict = result["parameters"]

        stu_list = "\n==== student list ====\n"
        for key, value in student_dict.items():
            stu_list += f"Name: {key}\n"
            for subject, score in value['scores'].items():
                stu_list += f"  subject: {subject}, score: {float(score)}\n"
            stu_list += "\n"
        stu_list += "\n======================"

        stu_list_label = QtWidgets.QLabel(stu_list, self.container_widget)
        stu_list_label.setStyleSheet("font-size: 24px;")
        self.container_layout.addWidget(stu_list_label)
        self.scroll_area.setWidget(self.container_widget)
