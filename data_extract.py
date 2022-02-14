import os
import requests 

## Função que realiza o download dos arquivos através de uma requisição web
def download_files(url, file, directory):
    print(f"Iniciando o Download em: {os.path.join(directory, file)}")
    ## Faz o request na URL
    response = requests.get(url)
    ## Verifica se a resposta da requisição foi sucesso
    if response.status_code == requests.codes.OK:
        ## Salva o arquivo
        with open(os.path.join(directory, file), 'wb') as nw_file:
                nw_file.write(response.content)
        print(f"Download finalizado. Arquivo salvo em: {os.path.join(directory, file)}")
    else:
        ## Caso tenha ocorrido uma falha na requisição, retorna esse erro
        response.raise_for_status()


