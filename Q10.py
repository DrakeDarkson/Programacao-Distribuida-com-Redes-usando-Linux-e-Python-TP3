import requests

URL = "http://127.0.0.1:8080"

response = requests.get(URL)

if response.status_code == 200:
    print("Página HTML recebida com sucesso!")
    print(response.text)
else:
    print(f"Erro ao acessar o servidor: {response.status_code}")
