import socket
import sys

HOST = '127.0.0.1'
PORT = 9003

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = sys.argv[1] if len(sys.argv) > 1 else input('Enter message: ')
    client.sendto(msg.encode(), (HOST, PORT))
    data, _ = client.recvfrom(1024)
    print('Server says:', data.decode())
    client.close()

if __name__ == '__main__':
    run_client()
