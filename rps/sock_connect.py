import socket

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

        :param str in_data:
        :param int packet_type:
        :return:
        """
        self.sock.send(self.format_packet(in_data, packet_type))
        while True:
            out_data = self.sock.recv(1024)
            print(out_data.decode(FORMAT))
            if out_data:
                break

    @staticmethod
    def format_packet(in_data, packet_type):
        return f'RPS{packet_type}{in_data}COMPLEX'.encode(FORMAT)






