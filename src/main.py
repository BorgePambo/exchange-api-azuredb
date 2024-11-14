import requests
import datetime
import pandas as pd
import os

# Defina a sua chave de API aqui
api_key = 'PFMFW1825XKYDIVB'  

url = 'https://www.alphavantage.co/query'
params = {
    'function': 'FX_DAILY',
    'from_symbol': 'USD',
    'to_symbol': 'BRL',
    'apikey': api_key, 
    'outputsize': 'full'  # Obter o máximo de dados disponíveis
}

response = requests.get(url, params=params)

# Verificar se a requisição foi bem-sucedida
def processar_dados():
    if response.status_code == 200:
        data = response.json()
        
        # Extrair a série temporal dos dados
        time_series = data.get('Time Series FX (Daily)', {})
        
        # Transformar os dados em DataFrame e ajustar o índice de datas
        df = pd.DataFrame(time_series).T  
        df.index = pd.to_datetime(df.index)  
        
        # Filtrar para os últimos 12 meses
        start_date = datetime.datetime.now() - datetime.timedelta(days=365)
        df_last_12_months = df[df.index >= start_date]

        # Exibir as taxas de fechamento para os últimos 12 meses
        df_last_12_months = df_last_12_months[['4. close']]  
        df_last_12_months.columns = ['USD/BRL']  
        
        return df_last_12_months


    else:
        print("Erro ao obter os dados:", response.status_code)
