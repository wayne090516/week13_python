from PyQt6.QtCore import QThread, pyqtSignal
from client.SocketClient import SocketClient
import json

# class ServiceController(QThread):
#     query_signal = pyqtSignal(str)
#     send_signal = pyqtSignal(str)
#     show_signal = pyqtSignal(str)

#     def __init__(self):
#         super().__init__()
#         self.client = SocketClient()
#         self.parameters = dict()

#     def query_stu(self, name):
#         response = Query(self.client,{"name":name}).execute()
#         self.query_signal.emit(response["status"])
    
#     def send_stu(self, parameters):
#         response = AddStu(self.client, parameters).execute()
#         self.send_signal.emit(response["status"])

#     def show_stu(self):
#         stu_list = ShowStu(self.client).execute()
#         self.show_signal.emit(stu_list)

class ServiceController():

    def __init__(self):
        self.socket_client = SocketClient()

    def command_sender(self, command, data):
        self.socket_client.send_command(command, data)
        result = self.socket_client.wait_response()

        return result


class ExecuteCommand(QThread):
    return_sig = pyqtSignal(str)

    def __init__(self, command, data):
        super().__init__()
        self.data = data
        self.command = command

    def run(self):
        result = ServiceController().command_sender(self.command, self.data)
        self.return_sig.emit(json.dumps(result))