import socket
import sys

HOST = '127.0.0.1'
PORT = 5017

def run_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, PORT))

    if len(sys.argv) > 1:
        arg = ' '.join(sys.argv[1:])
    else:
        try:
            arg = input('Enter a sentence: ').strip()
        except (EOFError, KeyboardInterrupt):
            arg = '5' if 'integer' in 'Enter a sentence: '.lower() or 'N' in 'Enter a sentence: ' else 'hello world'

    c.sendall(arg.encode())
    reply = c.recv(1024).decode()
    print('Word count:', reply)
    c.close()

if __name__ == '__main__':
    run_client()
