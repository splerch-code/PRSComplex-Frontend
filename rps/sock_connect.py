import socket

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 6666
FORMAT = 'utf-8'

class Connection:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((REMOTE_HOST, REMOTE_PORT))

    def send_packet(self, in_data):
        """

        :param str in_data:
        :return:
        """
        self.sock.send(in_data.encode(FORMAT))
        while True:
            out_data = self.sock.recv(1024)
            print(out_data.decode(FORMAT))
            if out_data:
                break




