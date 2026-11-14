import socket

HOST = '127.0.0.1'
PORT = 6012

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f'UDP Palindrome Server listening on {HOST}:{PORT}...')

    raw_data, addr = server.recvfrom(1024)
    data = raw_data.decode().strip()
    reply = "Palindrome" if data == data[::-1] else "Not a palindrome"
    server.sendto(reply.encode(), addr)
    server.close()

if __name__ == '__main__':
    start_server()
