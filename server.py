import threading
from networkstatic import*
import pickle
from player import Player

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((m_server, port))
client_lock = threading.Lock()
clients = set()
m_players = {} 

def handel_connection(conn, counter):
    conn.send(str.encode(str(counter)))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            if type(data) is utext:
                with client_lock:
                    for c in clients:
                        if c is not conn:
                            c.sendall(pickle.dumps(data))
            else:
                m_players[data.key] = data
                with client_lock:
                    for c in clients:
                        if c is not conn:
                            c.sendall(pickle.dumps(m_players))
        except:
            print("Lost connection")
            break

server.listen()
def start():
    counter = 0
    while True:
        conn, addr = server.accept()
        print(f'{addr} has connected')
        with client_lock:
            clients.add(conn)
        thread = threading.Thread(target=handel_connection, args=(conn, counter))
        thread.start()
        counter+=1

print("server [Running]")
start()
