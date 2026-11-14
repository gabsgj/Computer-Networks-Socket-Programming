import socket
import sys

HOST = '127.0.0.1'
PORT = 6016

def run_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if len(sys.argv) > 1:
        arg = ' '.join(sys.argv[1:])
    else:
        try:
            arg = input('Enter a message: ').strip()
        except (EOFError, KeyboardInterrupt):
            arg = '42' if 'integer' in 'Enter a message: '.lower() else 'networking in python'

    c.sendto(arg.encode(), (HOST, PORT))
    reply, _ = c.recvfrom(1024)
    print('Modified message:', reply.decode())
    c.close()

if __name__ == '__main__':
    run_client()
