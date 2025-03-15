import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Digite uma mensagem (ou 'sair' para fechar): ")
    client_socket.sendto(message.encode(), (HOST, PORT))

    if message.lower() == "sair":
        break

    data, _ = client_socket.recvfrom(1024)
    print(f"Servidor: {data.decode()}")

client_socket.close()
