import socket
import sys

HOST = 'localhost'
PORT = 8001

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if len(sys.argv) > 1:
        messages = [sys.argv[1]]
    else:
        print("Type 'time' to query current time or 'stop' to terminate the server.")
        messages = None

    if messages:
        for msg in messages:
            client.sendto(msg.encode(), (HOST, PORT))
            reply, _ = client.recvfrom(2048)
            print(f'Server reply: {reply.decode()}')
    else:
        while True:
            try:
                msg = input("Enter query ('time' or 'stop' to quit): ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if not msg:
                continue
            client.sendto(msg.encode(), (HOST, PORT))
            reply, _ = client.recvfrom(2048)
            print(f'Server reply: {reply.decode()}')
            if msg.lower() == 'stop':
                break

    client.close()

if __name__ == '__main__':
    run_client()
