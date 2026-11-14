import socket
from datetime import datetime

HOST = 'localhost'
PORT = 8001

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f'UDP Time Server listening on {HOST}:{PORT}...')

    while True:
        msg, addr = server.recvfrom(2048)
        decoded = msg.decode().strip()
        print(f'Received message from {addr}: "{decoded}"')

        if decoded.lower() == 'stop':
            print('Stop command received. Shutting down server.')
            server.sendto(b'Server stopped.', addr)
            break

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        server.sendto(current_time.encode(), addr)

    server.close()

if __name__ == '__main__':
    start_server()
