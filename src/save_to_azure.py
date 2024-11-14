import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


def conectar_azure_sqlalchemy():
    server = 'appserverdb2024.database.windows.net'  
    database = 'AzureApp'  
    username = 'sqladmin'  
    password = 'Brasil2024'  
    driver = 'ODBC Driver 18 for SQL Server'  

    # Formatar a URL de conexão
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver={driver}"

    engine = create_engine(connection_string)

    return engine


# Função para salvar os dados no banco de dados usando SQLAlchemy
def salvar_dados_sqlalchemy():
 
    df = pd.read_csv('clean/usd_brl_last_12_months.csv')

    # Conectar ao banco de dados SQL Server no Azure
    engine = conectar_azure_sqlalchemy()

   
    df.to_sql('cambioDb', con=engine, if_exists='replace', index=True, index_label='Data')

    print("Dados salvos no banco de dados com sucesso!")

if __name__ == "__main__":
    salvar_dados_sqlalchemy()