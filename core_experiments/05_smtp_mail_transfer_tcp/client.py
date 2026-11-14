import socket
import sys

HOST = '127.0.0.1'
PORT = 5025

def send_and_receive(sock, command):
    print(f'Client: {command}')
    sock.send((command + '\r\n').encode())
    response = sock.recv(1024).decode().strip()
    print(f'Server: {response}')
    return response

def run_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print('========== SMTP CLIENT ==========')
    initial_banner = sock.recv(1024).decode().strip()
    print(f'Server: {initial_banner}')

    send_and_receive(sock, 'HELO')

    if len(sys.argv) >= 5:
        sender = sys.argv[1]
        receiver = sys.argv[2]
        subject = sys.argv[3]
        body = ' '.join(sys.argv[4:])
    else:
        try:
            sender = input('Enter From address: ').strip() or 'alice@example.com'
            receiver = input('Enter To address: ').strip() or 'bob@example.com'
            subject = input('Enter Subject: ').strip() or 'Test Email'
            print("Enter email content. Type 'END' on a separate line when done:")
            lines = []
            while True:
                line = input()
                if line.strip() == 'END':
                    break
                lines.append(line)
            body = '\n'.join(lines) if lines else 'Hello, this is a test SMTP message!'
        except (EOFError, KeyboardInterrupt):
            sender = 'alice@example.com'
            receiver = 'bob@example.com'
            subject = 'Test Subject'
            body = 'Hello world from SMTP automated client.'

    send_and_receive(sock, f'MAIL FROM:<{sender}>')
    send_and_receive(sock, f'RCPT TO:<{receiver}>')
    send_and_receive(sock, 'DATA')

    email_payload = f'From: {sender}\r\nTo: {receiver}\r\nSubject: {subject}\r\n\r\n{body}\r\n.\r\n'
    sock.send(email_payload.encode())
    data_response = sock.recv(1024).decode().strip()
    print(f'Server: {data_response}')

    send_and_receive(sock, 'QUIT')
    sock.close()

if __name__ == '__main__':
    run_client()
