from datetime import datetime, timezone
import ssl
import socket

def verificar_certificado(hostname, port=443):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.connect((hostname, port))
    certificado = conn.getpeercert()

    print(f"Informações do certificado de segurança para {hostname}:\n")
    print(f"Emissor: {certificado['issuer']}")
    print(f"Assunto: {certificado['subject']}")
    validade_inicial = certificado['notBefore']
    validade_final = certificado['notAfter']
    print(f"Válido de: {validade_inicial}")
    print(f"Válido até: {validade_final}")

    validade_inicial = datetime.strptime(validade_inicial, "%b %d %H:%M:%S %Y GMT").replace(tzinfo=timezone.utc)
    validade_final = datetime.strptime(validade_final, "%b %d %H:%M:%S %Y GMT").replace(tzinfo=timezone.utc)
    data_atual = datetime.now(timezone.utc)

    if validade_inicial <= data_atual <= validade_final:
        print("O certificado está dentro do período de validade.")
    else:
        print("O certificado NÃO está mais válido.")

    if 'subjectAltName' in certificado:
        print(f"Outros nomes de assunto (SAN): {certificado['subjectAltName']}")
    conn.close()

if __name__ == "__main__":
    hostname = input("Digite o hostname ou IP do servidor HTTPS: ")
    verificar_certificado(hostname)
