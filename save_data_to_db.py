import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd
import configparser

## Função para realizar o salvamento dos dados no banco de dados
def save_file_to_db(files, directory):
    ## Pega as informações para a conexão ao banco
    config_path = 'config_mysql_db.ini'
    config = configparser.ConfigParser()
    config.read(config_path)
    db_host = config['database_connection']['HOST']
    db_user = config['database_connection']['DB_USER']
    db_password = config['database_connection']['DB_PASSWORD']
    db_use = config['database_connection']['DB_USE']

    print("Realizando a conexão com o banco de dados")
    ## Realiza a conexão com o banco de dados
    engine = sqlalchemy.create_engine(f"mysql://{db_user}:{db_password}@{db_host}")
    
    ## Verifica se existe um banco de dados para o armazenamento. Caso não, cria um
    with engine.connect() as connection:
        connection.execute(f"CREATE DATABASE IF NOT EXISTS {db_use};")
    ## Encerra a conexão
    connection.close()
    ## Finaliza a engine
    engine.dispose()

    ## Inicializa novamente a engine, mas agora acessando o banco
    engine = sqlalchemy.create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_use}")

    ## Estabelece a conexão
    with engine.connect() as connection:
        ## Pecorre a lista de arquivos para salvar
        for i in files:
            name = i.split(".")[0]
            print(f"Salvando a tabela {name}")
            ## Exclui a tabela se ela existir
            connection.execute(f"DROP TABLE IF EXISTS {name};")
            ## Vai salvando o arquivo em pedaços (100000 linhas por vez)
            for chunk in pd.read_csv(os.path.join(directory, i), chunksize=100000, dtype=object):
                print("Salvando 100000 registros")
                chunk.to_sql(name=name, con=connection, if_exists='append')
            print(f"Tabela {name} salva com sucesso!")
    ## Fecha a conexão
    connection.close()
    ## Encerra a engine
    engine.dispose() 

