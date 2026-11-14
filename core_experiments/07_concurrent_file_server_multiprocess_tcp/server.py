import socket
import multiprocessing
import os

HOST = '0.0.0.0'
PORT = 7200

def handle_client(conn, addr):
    try:
        filename = conn.recv(1024).decode().strip()
        print(f'Process PID {os.getpid()} handling request for: "{filename}" from {addr}')

        if os.path.exists(filename) and os.path.isfile(filename):
            with open(filename, 'r', errors='ignore') as f:
                content = f.read()
            response = f'Server PID: {os.getpid()}\n\n--- Contents of {filename} ---\n{content}'
        else:
            response = f'Server PID: {os.getpid()}\nFile "{filename}" not found.'

        conn.sendall(response.encode())
    except Exception as e:
        conn.sendall(f'Server PID: {os.getpid()}\nError: {e}'.encode())
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f'Concurrent File Server (Multiprocessing) listening on {HOST}:{PORT}...')
    print(f'Master Process PID: {os.getpid()}')

    try:
        while True:
            conn, addr = server.accept()
            p = multiprocessing.Process(target=handle_client, args=(conn, addr))
            p.daemon = True
            p.start()
            conn.close()
    except KeyboardInterrupt:
        print('\nShutting down file server.')
    finally:
        server.close()

if __name__ == '__main__':
    start_server()
