import http.server
import socketserver
import ssl

PORT = 8443

html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste de Servidor HTTPS</title>
</head>
<body>
    <h1>Bem-vindo ao servidor HTTPS!</h1>
    <p>Este é um exemplo de servidor HTTPS simples em Python.</p>
</body>
</html>
"""

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

httpd = socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler)
print(f"Servidor HTTPS rodando na porta {PORT}...")

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server-cert.pem", keyfile="server-key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

httpd.serve_forever()
