from PyQt6 import QtWidgets, QtGui, QtCore
from WorkWidgets.WidgetComponents import LabelComponent, LineEditComponent, ButtonComponent
import time
from PyQt6.QtCore import pyqtSignal
import json
from client.ServiceCtrl import ServiceCtrl

class AddStuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("add_stu_widget")
        layout = QtWidgets.QGridLayout()
        self.scores = {}
        header_label = LabelComponent(20, "Add Student")
        self.service_ctrl = ServiceCtrl()

        # ------label & editor-----------------------------------------------------
        # name
        name_label = LabelComponent(16, "Name: ")
        self.editor_label_name = LineEditComponent("Name")
        self.editor_label_name.mousePressEvent = self.clear_editor_name
        self.editor_label_name.textChanged.connect(self.name_change)
        # subject
        subject_label = LabelComponent(16, "Subject: ")
        self.editor_label_subject = LineEditComponent("Subject")
        self.editor_label_subject.mousePressEvent = self.clear_editor_subject
        # score
        score_label = LabelComponent(16, "Score: ")
        self.editor_label_score = LineEditComponent("")
        self.editor_label_score.setValidator(QtGui.QIntValidator(0, 100))

        # ------button-------------------------------------------------------------
        # query
        self.button_query = ButtonComponent("query")
        self.button_query.clicked.connect(self.query_act)
        # add
        self.button_add = ButtonComponent("add")
        self.button_add.clicked.connect(self.add_act)
        # send
        self.button_send = ButtonComponent("send")
        self.button_send.clicked.connect(self.send_act)

        self.message_label = LabelComponent(16, "")  # msg 

        # ------layout-------------------------------------------------------------
        layout.addWidget(header_label, 0, 0, 1, 2)  # header
        # label
        layout.addWidget(name_label, 1, 0, 1, 1)
        layout.addWidget(subject_label, 2, 0, 1, 1)
        layout.addWidget(score_label, 3, 0, 1, 1)
        # editor
        layout.addWidget(self.editor_label_name, 1, 1, 1, 1)
        layout.addWidget(self.editor_label_subject, 2, 1, 1, 1)
        layout.addWidget(self.editor_label_score, 3, 1, 1, 1)
        # button
        layout.addWidget(self.button_query, 1, 2, 1, 1)
        layout.addWidget(self.button_add, 3, 2, 1, 1)
        layout.addWidget(self.button_send, 5, 3, 1, 1)
        layout.addWidget(self.message_label, 4, 1, 1, 4)

        # ------row & column-------------------------------------------------------
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        layout.setColumnStretch(2, 4)
        layout.setColumnStretch(3, 4)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 2)
        layout.setRowStretch(2, 2)
        layout.setRowStretch(3, 2)
        layout.setRowStretch(4, 7)
        layout.setRowStretch(5, 5)

        self.setLayout(layout)
        self.load()

    def load(self):
        self.editor_label_name.setText("Name")
        self.editor_label_name.setEnabled(True)
        self.editor_label_subject.setText("Subject")
        self.editor_label_subject.setEnabled(False)
        self.editor_label_score.setText("")
        self.editor_label_score.setEnabled(False)
        self.button_query.setEnabled(False)
        self.button_add.setEnabled(False)
        self.button_send.setEnabled(False)
        self.scores = {}
        print("add widget")

    def clear_editor_name(self, event):
        self.editor_label_name.clear()

    def name_change(self, text):
        self.button_query.setEnabled(bool(text))

    def clear_editor_subject(self, event):
        self.editor_label_subject.clear()

    def query_act(self):
        if self.editor_label_name.text():
            name = self.editor_label_name.text()
            response = self.service_ctrl.query(name)
            if response.get('status') == 'failed':
                self.message_label.setText(f"{name} does not exist")
                self.editor_label_name.setEnabled(False)
                self.button_add.setEnabled(True)
                self.editor_label_subject.setEnabled(True)
                self.editor_label_score.setEnabled(True)
            else:
                self.message_label.setText(f"{name} does exist")

    def add_act(self):
        if not self.editor_label_name.text().strip() or not self.editor_label_subject.text().strip() or not self.editor_label_score.text().strip():
            self.message_label.setText("Name, Subject and Score cannot be empty.")
        else:
            name = self.editor_label_name.text()
            subject = self.editor_label_subject.text()
            score = self.editor_label_score.text()

            if name not in self.scores:
                self.scores[name] = {}

            if subject in self.scores[name]:
                self.message_label.setText(f"The subject {subject} is already in the records for student {name}.")
            else:
                self.scores[name][subject] = score                
                self.message_label.setText(f"Name: {name},\nSubject: {subject},\nScore: {score}")
                self.button_send.setEnabled(True)

    def send_act(self):
        name = self.editor_label_name.text()
        score = self.scores.get(name)
        if score is not None:
            response = self.service_ctrl.send('add', {'name': name, 'scores': self.scores[name]})
            self.scores.pop(name, None)
            self.message_label.setText("Student scores successfully sent.")
        else:
            self.message_label.setText("No score to send.")
        self.load()
