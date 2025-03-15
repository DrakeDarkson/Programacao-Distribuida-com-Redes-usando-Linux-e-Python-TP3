import socket

HOST = "127.0.0.1"
PORT = 12345

def upload_file(client_socket):
    filename = input("Digite o nome do arquivo para upload: ")
    client_socket.send(filename.encode())
    client_socket.recv(1024)

    client_socket.send(b"upload")

    try:
        with open(filename, "rb") as f:
            print(f"Enviando o arquivo: {filename}")
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.send(data)
            print(f"Arquivo {filename} enviado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

def download_file(client_socket):
    filename = input("Digite o nome do arquivo para download: ")
    client_socket.send(filename.encode())
    client_socket.recv(1024)

    client_socket.send(b"download")

    data = client_socket.recv(1024)
    if data == "Arquivo não encontrado.":
        print("Arquivo não encontrado no servidor.")
    else:
        with open(f"downloaded_{filename}", "wb") as f:
            print(f"Recebendo o arquivo: {filename}")
            while data:
                f.write(data)
                data = client_socket.recv(1024)
            print(f"Arquivo {filename} recebido com sucesso!")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        action = input("Digite 'upload' para enviar um arquivo ou 'download' para baixar um arquivo ('sair' para sair): ").lower()
        if action == 'sair':
            break
        elif action == 'upload':
            upload_file(client_socket)
        elif action == 'download':
            download_file(client_socket)
        else:
            print("Opção inválida! Tente novamente.")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
