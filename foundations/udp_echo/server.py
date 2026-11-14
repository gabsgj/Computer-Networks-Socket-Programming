import socket

HOST = '127.0.0.1'
PORT = 9003

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f'UDP Echo Server listening on {HOST}:{PORT}...')

    data, addr = server.recvfrom(1024)
    print(f'Received from {addr}: {data.decode()}')
    server.sendto(b'Echo: ' + data, addr)
    server.close()

if __name__ == '__main__':
    start_server()
