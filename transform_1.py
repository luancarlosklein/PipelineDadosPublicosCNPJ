from zipfile import ZipFile
import pandas as pd
import os
import io

## Função que faz a padronização: Do arquivo zip para um csv
def data_standardization(directory_file_open, file_open, directory_file_save, name_file_save):
    ## Cria uma variável para armazenar os arquivos em Bytes
    ## Faz isso por causa do formato dos arquivos
    temp_arm_file = io.BytesIO()
    
    print(f"Inicio da Padronização | Arquivo Aberto - {file_open}")
    
    # Descompactando Arquivo Zip na váriavel de bytes
    with ZipFile(os.path.join(directory_file_open, file_open), 'r') as zip_ref:
        temp_arm_file.write(zip_ref.read(zip_ref.namelist()[0]))
            
    # Volta o indicador do arquivo para o inicio
    temp_arm_file.seek(0)

    ## Apaga o arquivo antigo (se existir)
    try:
        os.remove(os.path.join(directory_file_save, name_file_save))
        print("Arquivo antigo removido!")
    except OSError as e:
        print("Nenhum arquivo encontrado para a exclusão!")

    # Faz a leitura do arquivo em csv
    for chunk in pd.read_csv(temp_arm_file, delimiter=';', header=None, dtype=str, encoding="ISO-8859-1", chunksize = 100000):
        chunk.to_csv(os.path.join(directory_file_save, name_file_save), mode='a', header=False, index=False)
        print("Salvando 100000 registros no arquivo")
    #df = pd.read_csv(temp_arm_file, delimiter=';', header=None, dtype=str, encoding="ISO-8859-1")
    
    #df.to_csv(os.path.join(directory_file_save, name_file_save))
    print(f"Fim da Padronização | Arquivo Salvo - {name_file_save}")



