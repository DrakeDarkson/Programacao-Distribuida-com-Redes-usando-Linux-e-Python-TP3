import socket

HOST = "0.0.0.0"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor UDP escutando na porta {PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Mensagem recebida de {addr}: {message}")

    if message.lower() == "sair":
        print("Encerrando servidor UDP...")
        break

    response = "Mensagem recebida com sucesso!"
    server_socket.sendto(response.encode(), addr)

server_socket.close()
