import socket

HOST = '127.0.0.1'
PORT = 9001

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f'TCP Echo Server listening on {HOST}:{PORT}...')

    conn, addr = server.accept()
    print(f'Connected by {addr}')
    data = conn.recv(1024)
    if data:
        print(f'Received: {data.decode()}')
        conn.sendall(b'Echo: ' + data)
    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
