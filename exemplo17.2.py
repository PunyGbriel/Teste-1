import requests
url = "https://pudim.com.br"
try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        print(f'O site {url} esta acessivel')

except requests.exceptions.RequestException as e:
    print(f'O {url} não pode ser acessivel!')