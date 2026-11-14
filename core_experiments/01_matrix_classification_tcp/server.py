import socket
import pickle

HOST = '0.0.0.0'
PORT = 9002

def classify_matrix(n, matrix):
    upper = True
    lower = True
    diagonal = True
    for i in range(n):
        for j in range(n):
            if i > j and matrix[i][j] != 0:
                upper = False
            if i < j and matrix[i][j] != 0:
                lower = False
            if i != j and matrix[i][j] != 0:
                diagonal = False

    if diagonal:
        return 'Diagonal Matrix'
    elif upper:
        return 'Upper Triangular Matrix'
    elif lower:
        return 'Lower Triangular Matrix'
    else:
        return 'Normal Matrix'

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f'Matrix Classification Server listening on {HOST}:{PORT}...')

    conn, addr = server.accept()
    print('Connected by client:', addr)
    data = pickle.loads(conn.recv(4096))
    n, matrix = data
    print(f'Received matrix of order {n} from client:')
    for row in matrix:
        print(*row)

    result = classify_matrix(n, matrix)
    print('Identified matrix type:', result)
    print('Sending result to client...')
    conn.send(result.encode())
    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
