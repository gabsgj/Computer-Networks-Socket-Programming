import socket

HOST = '127.0.0.1'
PORT = 9010

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f'TCP Calculator Server listening on {HOST}:{PORT}...')

    conn, addr = server.accept()
    print(f'Connected by {addr}')

    while True:
        data = conn.recv(1024).decode().strip()
        if not data or data.lower() == 'exit':
            break
        print(f'Received expression: {data}')
        try:
            tokens = data.split()
            if len(tokens) == 3:
                a, op, b = float(tokens[0]), tokens[1], float(tokens[2])
                if op == '+': result = str(a + b)
                elif op == '-': result = str(a - b)
                elif op == '*': result = str(a * b)
                elif op == '/': result = str(a / b) if b != 0 else 'Error: division by zero'
                else: result = 'Error: unknown operator'
            else:
                result = 'Error: format must be <num> <op> <num>'
        except Exception as e:
            result = f'Error: {e}'

        conn.sendall(result.encode())

    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
