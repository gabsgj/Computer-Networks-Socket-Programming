import socket
import threading

HOST = '0.0.0.0'
PORT = 9022

clients = []
clients_lock = threading.Lock()

def broadcast(message, sender_conn):
    with clients_lock:
        disconnected = []
        for client in clients:
            if client != sender_conn:
                try:
                    client.sendall(message)
                except OSError:
                    disconnected.append(client)
        for dead_client in disconnected:
            if dead_client in clients:
                clients.remove(dead_client)
            dead_client.close()

def handle_client(conn, addr):
    print(f'New client connected: {addr}')
    with clients_lock:
        clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'[{addr[0]}:{addr[1]}] {data.decode().strip()}')
            broadcast(data, conn)
    except OSError:
        pass
    finally:
        with clients_lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()
        print(f'Client {addr} disconnected.')

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(10)
    print(f'Multi-Client Chat Server listening on {HOST}:{PORT}...')

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print('
Shutting down chat server.')
    finally:
        server.close()

if __name__ == '__main__':
    start_server()
