Currency API to Azure SQL

Este projeto tem como objetivo obter dados de taxas de câmbio diárias da API Alpha Vantage e armazená-los em um banco de dados SQL Server hospedado na Azure.
Funcionalidade principal

    Obtenção de dados: O projeto utiliza a API da Alpha Vantage para buscar a cotação diária de moedas, especificamente a taxa de câmbio USD/BRL.
    Processamento dos dados: Após a coleta, os dados são filtrados para os últimos 12 meses e preparados para armazenamento.
    Armazenamento no banco de dados: Os dados de câmbio são então armazenados em um banco de dados SQL Server hospedado na Azure.

Estrutura do Projeto

    Python: Utiliza-se o Python como linguagem principal para integração com a API, processamento de dados e interação com o banco de dados.
    SQLAlchemy & PyODBC: São usados para conectar e interagir com o banco de dados SQL Server na Azure.
    Dotenv: Utilizado para gerenciar variáveis de ambiente (como credenciais de banco de dados) de forma segura, sem a necessidade de codificar diretamente informações sensíveis.

Como Funciona:

    O script consulta a API Alpha Vantage para obter as taxas de câmbio diárias para a conversão USD para BRL.
    Os dados são filtrados para mostrar apenas as taxas dos últimos 12 meses.
    Esses dados são então armazenados em uma tabela SQL Server hospedada na Azure, permitindo consultas e análise futura.

Tecnologias Utilizadas

    Python 3.x
    SQLAlchemy
    Alpha Vantage API
    Azure SQL Database
    dotenv

Segurança

    O projeto utiliza o arquivo .env para armazenar credenciais de banco de dados, mantendo informações sensíveis fora do repositório público.
    Certifique-se de nunca fazer upload do arquivo .env para o repositório.
