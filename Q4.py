import socket

def scan_port(host, port):
    """Tenta conectar ao host na porta especificada."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((host, port))
        print(f"[+] Porta {port} aberta")
    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        sock.close()

def scan_ports(host, start_port, end_port):
    """Escaneia um intervalo de portas no host especificado."""
    print(f"Escaneando {host} de {start_port} até {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio do alvo: ")
    porta_inicial = int(input("Digite a porta inicial: "))
    porta_final = int(input("Digite a porta final: "))

    scan_ports(alvo, porta_inicial, porta_final)
