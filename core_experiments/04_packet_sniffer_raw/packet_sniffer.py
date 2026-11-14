import socket
import sys
import os

def format_mac(bytes_addr):
    return ':'.join(f'{b:02x}' for b in bytes_addr)

def format_ip(bytes_addr):
    return socket.inet_ntoa(bytes_addr)

def run_sniffer():
    # Raw socket with AF_PACKET is standard on Linux.
    # Requires administrative privileges (sudo/root).
    if not hasattr(socket, 'AF_PACKET'):
        print('[ERROR] socket.AF_PACKET is only supported on Linux kernels.')
        print('On macOS and BSD systems, packet capturing requires BPF (/dev/bpf*) or AF_INET SOCK_RAW.')
        print('To run this script on Linux, execute:')
        print('    sudo python3 packet_sniffer.py')
        return

    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    except PermissionError:
        print('[ERROR] Permission denied: Raw sockets require root/administrative privileges.')
        print('Run with: sudo python3 packet_sniffer.py')
        return

    print('Packet Capturer Started...')
    print('Listening for Ethernet frames (press Ctrl+C to stop)...')

    packet_count = 0
    try:
        while True:
            data, addr = s.recvfrom(65535)
            packet_count += 1
            print('-' * 60)
            print(f'Packet #{packet_count} Received')
            print(f'Packet Length   : {len(data)} bytes')
            print('First 20 Bytes  :', ' '.join(f'{b:02x}' for b in data[:20]))

            # Ethernet Header (14 bytes: 6 dest MAC + 6 src MAC + 2 EtherType)
            dest_mac = format_mac(data[0:6])
            src_mac = format_mac(data[6:12])
            eth_type = int.from_bytes(data[12:14], 'big')

            print(f'Source MAC      : {src_mac}')
            print(f'Destination MAC : {dest_mac}')
            print(f'Ethernet Type   : {hex(eth_type)}')

            # Check for IPv4 (0x0800)
            if eth_type == 0x0800 and len(data) >= 34:
                ttl = data[22]
                ip_protocol = data[23]
                src_ip = format_ip(data[26:30])
                dest_ip = format_ip(data[30:34])

                proto_name = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}.get(ip_protocol, str(ip_protocol))

                print(f'Source IP       : {src_ip}')
                print(f'Destination IP  : {dest_ip}')
                print(f'TTL             : {ttl}')
                print(f'Protocol        : {proto_name}')
    except KeyboardInterrupt:
        print('Sniffer stopped by user.')
    finally:
        s.close()

if __name__ == '__main__':
    run_sniffer()