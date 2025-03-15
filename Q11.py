import socket
import os

HOST = "127.0.0.1"
PORT = 12345
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def handle_client(client_socket):
    try:
        filename = client_socket.recv(1024).decode()
        if filename:
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            client_socket.send(b"OK")

            action = client_socket.recv(1024).decode()
            if action == "upload":
                with open(filepath, 'wb') as f:
                    print(f"Recebendo o arquivo: {filename}")
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        f.write(data)
                    print(f"Arquivo {filename} recebido com sucesso!")

            elif action == "download":
                if os.path.exists(filepath):
                    with open(filepath, 'rb') as f:
                        client_socket.send(f.read())
                        print(f"Enviando o arquivo: {filename}")
                else:
                    client_socket.send("Arquivo não encontrado.")
                    print(f"Arquivo {filename} não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Servidor de arquivos rodando em {HOST}:{PORT}...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()
