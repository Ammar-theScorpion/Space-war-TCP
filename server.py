import threading
from networkstatic import*
import pickle
from player import Player

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((m_server, port))

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((m_server, port))

client_lock = threading.Lock()
clients = set()
m_players = {} 

def handel_connection(conn, counter):
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            if not data:
                    break
            if type(data) is utext:
                with client_lock:
                    for c in clients:
                        if c is not conn:
                            c.sendall(pickle.dumps(data))
            else:
                m_players[counter] = data
                conn.sendall(pickle.dumps(m_players))
        except:
            break

    print("Lost connection")
    try:
        del m_players[counter]
        print("Closing Game", counter)
    except:
        pass
    conn.close()

server.listen()
def start():
    counter = 0
    r_counter = 0
    while True:
        conn, addr = server.accept()
        if counter%2==0:
            r_counter+=1
        print(f'{addr} has connected')
        with client_lock:
            clients.add(conn)
        print(r_counter)
        thread = threading.Thread(target=handel_connection, args=(conn, counter))
        thread.start()
        counter+=1

def receive():
    thread = threading.Thread(target=start, args=())
    thread.start()
    while True:
        try:
            
            data, addr = udp_server.recvfrom(2048)
            data = pickle.loads(data)
            m_players[addr] = data
            udp_server.sendto(pickle.dumps(m_players), addr)

        except:
            pass
print("server [Running]")
receive()
