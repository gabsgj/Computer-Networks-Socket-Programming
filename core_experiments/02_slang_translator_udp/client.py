import socket
import sys

HOST = 'localhost'
PORT = 9000

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    else:
        try:
            message = input('Enter sentence: ')
        except (EOFError, KeyboardInterrupt):
            message = 'tbh idk what to do rn, brb'

    client.sendto(message.encode(), (HOST, PORT))
    translated, _ = client.recvfrom(2048)
    print('\nTranslated Sentence:\n' + translated.decode())
    client.close()

if __name__ == '__main__':
    run_client()
