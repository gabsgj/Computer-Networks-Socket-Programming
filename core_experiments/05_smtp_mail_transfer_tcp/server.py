import socket

HOST = '127.0.0.1'
PORT = 5025

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f'SMTP Simulation Server started on {HOST}:{PORT}...')
    print('Waiting for client connection...\n')

    conn, addr = server.accept()
    print(f'Client connected from: {addr}')
    conn.send(b'220 SMTP Server Ready\r\n')

    email_buffer = ''
    in_data_mode = False

    while True:
        data = conn.recv(1024)
        if not data:
            break

        lines = data.decode().splitlines()
        for line in lines:
            line_str = line.strip()
            print(f'Client: {line_str}')

            if in_data_mode:
                if line_str == '.':
                    in_data_mode = False
                    print('\n========== RECEIVED EMAIL ==========')
                    print(email_buffer.strip())
                    print('====================================\n')
                    conn.send(b'250 Email received successfully\r\n')
                    email_buffer = ''
                else:
                    email_buffer += line + '\n'
            else:
                if line_str == 'HELO' or line_str.startswith('EHLO'):
                    conn.send(b'250 Hello, welcome to the SMTP server\r\n')
                elif line_str.startswith('MAIL FROM:'):
                    conn.send(b'250 Sender OK\r\n')
                elif line_str.startswith('RCPT TO:'):
                    conn.send(b'250 Recipient OK\r\n')
                elif line_str == 'DATA':
                    in_data_mode = True
                    conn.send(b'354 Start mail input; end with <CRLF>.<CRLF>\r\n')
                elif line_str == 'QUIT':
                    conn.send(b'221 Goodbye, closing transmission channel\r\n')
                    conn.close()
                    server.close()
                    print('Server closed successfully.')
                    return
                else:
                    conn.send(b'500 Unknown command\r\n')

    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
