import requests

URL = "https://127.0.0.1:8443"

response = requests.get(URL, verify=False)

if response.status_code == 200:
    print("Página HTML recebida com sucesso!")
    print(response.text)
else:
    print(f"Erro ao acessar o servidor: {response.status_code}")
