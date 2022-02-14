import pandas as pd
import os

## Função para o ajuste dos dados corretamente
def data_conformation(directory_file_open, file_open, directory_file_save, name_file_save):
    ## Pega o nome de quem está sendo processado
    name = file_open.split('.')[0]
    ## Colunas de cada um dos arquivos 
    data_layout = {
        "socios" : {"colunas" : ["cnpj_base", "tipo", "nome", "cpf_cnpj", "qualificacao", "data_entrada",
                                 "pais", "cpf_representante", "nome_representante", "qualificacao_representante",
                                 "faixa_etaria"]},
        "empresa" : {"colunas" : ["cnpj_base", "razao_social", "natureza_juridica", "qualificacao",
                                  "capital_social", "porte_empresa", "ente_federativo"]},
        "estabelecimento" : {"colunas" : ["cnpj_base", "cnpj_ordem", "cnpj_dv", "matriz_filial", "nome_fantasia", "situacao_cadastral",
                                  "data_situacao_cadastral", "motivo_situacao_cadastral", "cidade_exterior", "pais", "inicio_atividade",
                                  "cnae_principal", "cnae_secundario", "tipo_logradouro", "logradouro", "numero", "complemento",
                                  "bairro", "cep", "uf", "municipio", "ddd1", "telefone1", "ddd2", "telefone2",
                                  "ddd_fax", "fax", "email", "situacao_especial", "data_situacao_especial"]}
        }
    
    print(f"Abrindo o arquivo e iniciando a conformação - {file_open}")

    ## Variável usada para verificar se está no primeiro chunk (por causa do cabeçalho)
    firstChunk = True
    
    ## Verifica quais campos são de datas (para preparar eles depois)
    colunas_use = []
    for i in data_layout[name]["colunas"]:
        if "data" in i:
            colunas_use.append(i)

    ## Apaga o arquivo antigo (se existir)
    try:
        os.remove(os.path.join(directory_file_save, name_file_save))
        print("Arquivo antigo removido!")
    except OSError as e:
        print("Nenhum arquivo encontrado para a exclusão!")  
    print (f"Iniciando o salvamento do arquivo - {file_open}")
    ##Devido ao tamanho dos arquivos, eles serão abertos e salvos em partes
    for chunk in pd.read_csv(os.path.join(directory_file_open, file_open), header=None, dtype=str, names=data_layout[name]["colunas"], chunksize = 100000, encoding="ISO-8859-1"):
        ## Percorre todos os campos de data
        for i in colunas_use:
            ## Preenche com Nulo quando for 0 ou 00000000
            chunk[i] = chunk[i].mask(chunk[i] == '0', None)
            chunk[i] = chunk[i].mask(chunk[i] == '00000000', None)
            ## Transforma o campo para data. E em caso de erro, o campo é setado como Nulo (errors=coerce)
            chunk[i] = pd.to_datetime(chunk[i], format='%Y%m%d', errors='coerce')
        
        print("Salvando 100000 registros no arquivo")
        ## Salva os csv preparado
        chunk.to_csv(os.path.join(directory_file_save, name_file_save),  mode='a', header = firstChunk, index=False)

        ## Verifica se é o primeiro chunk (para salvar o cabeçalho)
        if firstChunk:
            firstChunk = False
    print (f"Finalizando o salvamento do arquivo - {file_open}")
    print(f"Conformação finalizada e arquivo salvo - {name_file_save}")
