import socket
import pickle
import random
import sys

HOST = '127.0.0.1'
PORT = 9002

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        try:
            n = int(input('Enter order of matrix: '))
        except (ValueError, EOFError):
            n = 3

    matrix = [[random.randint(1, 50) for _ in range(n)] for _ in range(n)]
    matrix_type = random.choice(['upper', 'lower', 'diagonal', 'normal'])

    if matrix_type == 'upper':
        for i in range(n):
            for j in range(n):
                if i > j:
                    matrix[i][j] = 0
    elif matrix_type == 'lower':
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j] = 0
    elif matrix_type == 'diagonal':
        for i in range(n):
            for j in range(n):
                if i != j:
                    matrix[i][j] = 0

    print(f'Generated ({matrix_type}) Matrix:')
    for row in matrix:
        print(*row)

    data = (n, matrix)
    client.send(pickle.dumps(data))
    result = client.recv(1024).decode()
    print('Matrix Type Received from Server:', result)
    client.close()

if __name__ == '__main__':
    run_client()
