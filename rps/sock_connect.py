import socket
import json

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 6666
FORMAT = 'utf-8'


class Connection:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Connecting to remote host')
        self.sock.connect((REMOTE_HOST, REMOTE_PORT))

    def send_packet(self, in_data, packet_type):
        """

        :param dict in_data:
        :param int packet_type:
        :return:
        """
        self.sock.send(self.format_packet(in_data, packet_type))
        while True:
            out_data = self.sock.recv(1024)
            print(out_data.decode(FORMAT))
            if out_data:
                break
        return json.loads(out_data)

    @staticmethod
    def format_packet(in_data, packet_type):
        return f'RPS{packet_type}{str(in_data)}COMPLEX'.encode(FORMAT)

    def create_account(self, username, email, password_hash):
        send_data = {
            'username': username,
            'email': email,
            'password_hash': password_hash
        }
        return self.send_packet(send_data, packet_type=2)
