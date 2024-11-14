import main as ma
import os


def salvando_em_csv():
    # Obter dados processados
    df_last_12_months = ma.processar_dados()

    # Checar se os dados foram obtidos com sucesso
    if df_last_12_months is not None:
        # Criar pasta "clean" e salvar o DataFrame em CSV
        os.makedirs('clean', exist_ok=True)
        df_last_12_months.to_csv('clean/usd_brl_12_months.csv')
        print("Arquivo salvo com sucesso em 'clean/usd_brl_last_12_months.csv'")
    else:
        print("Não foi possível salvar os dados.")



# Executar a função para salvar o CSV
if __name__ == "__main__":
    salvando_em_csv()