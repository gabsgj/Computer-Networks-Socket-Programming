import socket
import re

HOST = 'localhost'
PORT = 9000

SLANG_DICTIONARY = {
    'tbh': 'To Be Honest',
    'ig': 'I guess',
    'tbf': 'To be fair',
    'atm': 'at the moment',
    'irl': 'in real life',
    'lol': 'Laugh out loud',
    'asap': 'as soon as possible',
    'omg': 'Oh my god',
    'ttyl': 'Talk to you later',
    'idk': "I don't know",
    'nvm': 'never mind',
    'idc': "I don't care",
    'iykyk': 'If you know you know',
    'brb': 'be right back',
    'btw': 'by the way'
}

def translate_slang(text):
    result = text
    for slang, expansion in SLANG_DICTIONARY.items():
        pattern = re.compile(r'\b' + re.escape(slang) + r'\b', re.IGNORECASE)
        result = pattern.sub(expansion, result)
    return result

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f'Slang Translator UDP Server listening on {HOST}:{PORT}...')

    try:
        while True:
            msg, addr = server.recvfrom(2048)
            sentence = msg.decode().strip()
            print(f'Received from {addr}: "{sentence}"')
            if sentence.lower() == '__shutdown__':
                break
            translated = translate_slang(sentence)
            print(f'Translated: "{translated}"')
            server.sendto(translated.encode(), addr)
    finally:
        server.close()
        print('Server stopped.')

if __name__ == '__main__':
    start_server()
