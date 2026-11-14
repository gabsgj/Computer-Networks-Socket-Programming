import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 9022

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print('
[Connection closed by server]')
                break
            print(data.decode().strip())
        except OSError:
            break

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    name = sys.argv[1] if len(sys.argv) > 1 else input('Enter your name: ').strip() or 'Anonymous'

    recv_thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    recv_thread.start()

    print(f"Connected as '{name}'. Type messages and press Enter. Type 'exit' to quit.")

    try:
        while True:
            msg = input()
            if not msg:
                continue
            if msg.lower() == 'exit':
                break
            formatted = f'[{name}]: {msg}
'
            sock.sendall(formatted.encode())
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        sock.close()
        print('Client exited.')

if __name__ == '__main__':
    run_client()
