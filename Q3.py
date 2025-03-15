import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

print("Aguardando pacotes ICMP...")
while True:
    packet, addr = sock.recvfrom(65535)
    print(f"Pacote recebido de {addr}: {packet.hex()}")
