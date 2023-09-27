import requests

url = 'https://www.google.com'

proxy = {'http': 'http://localhost:3128', 'https': 'http://localhost:3128'}

try:
    response = requests.get(url, proxies=proxy)
    
    if response.status_code == 200:
        print("A proxy está funcionando corretamente.")
    else:
        print("A solicitação não foi bem-sucedida. Verifique sua configuração de proxy.")
except Exception as e:
    print(f"Erro ao acessar a URL através da proxy: {str(e)}")