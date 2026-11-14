import socket
import sys

HOST = '127.0.0.1'
PORT = 7200

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        try:
            filename = input('Enter filename to request: ').strip() or 'sample.txt'
        except (EOFError, KeyboardInterrupt):
            filename = 'sample.txt'

    sock.sendall(filename.encode())
    response = sock.recv(65536).decode()
    print('--- Response from File Server ---')
    print(response)
    sock.close()

if __name__ == '__main__':
    run_client()
