import pickle
from networkstatic import*
class Network:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pos = self.connect()

    def connect(self):
        (self.server.connect((m_server, port)))
        return self.server.recv(2048).decode()

    def get_key(self):
        print(self.pos)
        return self.pos

    def send(self, data):
        self.server.send(pickle.dumps(data))
        return pickle.loads(self.server.recv(2048*16))

    def get(self):
        return pickle.loads(self.server.recv(2048*16))

