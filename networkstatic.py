import socket
import threading

m_server = socket.gethostbyname(socket.gethostname()) 
port = 5998
class utext:
    def __init__(self, text, ctime):
        self.text = text
        self.ctime = ctime