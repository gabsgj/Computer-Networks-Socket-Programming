import socket
import sys

HOST = '127.0.0.1'
PORT = 9001

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    msg = sys.argv[1] if len(sys.argv) > 1 else input('Enter message: ')
    client.sendall(msg.encode())
    data = client.recv(1024)
    print('Server says:', data.decode())
    client.close()

if __name__ == '__main__':
    run_client()
