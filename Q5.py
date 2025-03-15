import socket

HOST = "0.0.0.0"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor TCP escutando na porta {PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "sair":
            print("Conexão encerrada pelo cliente.")
            break
        print(f"Cliente: {data}")
        conn.sendall("Mensagem recebida!\n".encode())

    conn.close()
