import http.server
import socketserver

PORT = 8080

html_content = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste de Servidor HTTP</title>
</head>
<body>
    <h1>Bem-vindo ao servidor HTTP!</h1>
    <p>Este é um exemplo de servidor HTTP simples em Python.</p>
</body>
</html>
"""

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Servidor HTTP rodando na porta {PORT}...")
    httpd.serve_forever()
