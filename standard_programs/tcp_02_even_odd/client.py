import socket
import sys

HOST = '127.0.0.1'
PORT = 5002

def run_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, PORT))

    if len(sys.argv) > 1:
        arg = ' '.join(sys.argv[1:])
    else:
        try:
            arg = input('Enter an integer: ').strip()
        except (EOFError, KeyboardInterrupt):
            arg = '5' if 'integer' in 'Enter an integer: '.lower() or 'N' in 'Enter an integer: ' else 'hello world'

    c.sendall(str(arg).encode())
    reply = c.recv(1024).decode()
    print('The number is:', reply)
    c.close()

if __name__ == '__main__':
    run_client()
