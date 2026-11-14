import socket
import sys

HOST = '127.0.0.1'
PORT = 9010

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    if len(sys.argv) > 1:
        expr = ' '.join(sys.argv[1:])
        client.sendall(expr.encode())
        print('Result:', client.recv(1024).decode())
        client.sendall(b'exit')
    else:
        while True:
            try:
                expr = input("Enter expression (<num> <op> <num>) or 'exit': ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not expr:
                continue
            client.sendall(expr.encode())
            if expr.lower() == 'exit':
                break
            print('Result:', client.recv(1024).decode())

    client.close()

if __name__ == '__main__':
    run_client()
