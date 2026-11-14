import socket

HOST = '127.0.0.1'
PORT = 5017

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f'Word Count Server listening on {HOST}:{PORT}...')

    conn, addr = server.accept()
    data = conn.recv(1024).decode().strip()
    reply = str(len(data.split()))
    conn.sendall(reply.encode())
    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
