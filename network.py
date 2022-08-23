import pickle
from networkstatic import*
class Network:
    def __init__(self, one):
        if one == 0:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            print('int')
            self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        (self.server.connect((m_server, port)))

    def sendto(self, data):
        try:

            self.server.sendto(pickle.dumps(data), (m_server, port))
            d, a =self.server.recvfrom(2048*16)
            return pickle.loads(d)
        except:
            pass

    def send(self, data):
        try:
            self.server.send(pickle.dumps(data))
            return pickle.loads(self.server.recv(2048*16))
        except:
            pass
    def get(self):
        return pickle.loads(self.server.recv(2048*16))

