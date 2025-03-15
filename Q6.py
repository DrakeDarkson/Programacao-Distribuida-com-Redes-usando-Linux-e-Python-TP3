import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    msg = input("Digite uma mensagem (ou 'sair' para fechar): ")
    client_socket.sendall(msg.encode())
    if msg.lower() == "sair":
        break
    response = client_socket.recv(1024).decode()
    print(f"Servidor: {response}")

client_socket.close()
