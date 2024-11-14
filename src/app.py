import requests



# URL da API com a sua chave de API
api_url = 'https://v6.exchangerate-api.com/v6/990d4140ab145ad637dac4f2/latest/USD'

# Fazendo a requisição para obter as taxas de câmbio
response = requests.get(api_url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    
    # Extraindo a taxa de câmbio do dólar (USD) para o real (BRL)
    usd_brl_rate = data['conversion_rates']['BRL']
    print("Taxa de câmbio do dólar (USD) para real (BRL):", usd_brl_rate)
else:
    print("Erro ao obter os dados:", response.status_code)