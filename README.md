##Introdução
O pipeline de processamento dos dados se encontra dividodo em 4 partes.
Cada uma dessas partes é realizada por um script separado. 
Todos esses scrips são organizados e osquestrados por um outro script, que serão detalhados abaixo.
Todos os códigos estão comentados e apresentam explicações.

---- O arquivo que deve ser executado para execução de todo o pipeline é o orchestrator.py. ----

## Scripts ##

# Parte 1: Coleta dos dados - data_extract.py
-- Esse script acessa a URL onde os dados estão disponíveis, e baixa os arquivos .zip disponibilizados.
-- É realizado o download apenas da parte 1 de cada um dos arquivos.
-- A função que faz o dowloado recebe 3 parametros: URL, nome do arquivo e a pasta em que será baixada.

# Parte 2: Padronização dos dados - transform_1.py
-- Esse script pega o .zip da pasta raw e salva em um .csv na pasta standardized
-- A função que faz esse processo recebe os nomes dos arquivos a serem abertos e salvos
-- e o nome das pastas de onde o arquivo está e para onde vai.

# Parte 3: Conformação dos dados - transform_2.py
-- Esse script pega o .csv da pasta standardized e salva em um .csv na pasta conformed
-- Pega o arquivo.csv salvo anteriormente, e prepara ele para ser salvo no banco de dados
-- Transforma as colunas de datas para ficarem padronizadas e coloca o nome de cada coluna.
-- A função que faz esse processo recebe os nomes dos arquivos a serem abertos e salvos
-- e o nome das pastas de onde o arquivo está e para onde vai.

# Parte 4: Salvamento dos dados no banco de dados - save_data_to_bd.py
-- Esse script pega os .csv salvos na pasta conformed e salva no banco de dados
-- As configurações para o acesso ao banco de dados e o nome do banco estão no arquivo 'config_mysql_db'

#Orquestrador - orchestrator.py
-- Script que chama cada uma das partes de maneira ordenada.
-- Além disso, é esse script que é chamado periodicamente para a execução de todo o processo.

##OBSERVAÇÕES
-- É necessário utilizar a versão 64bits do python, devido ao tamanho dos arquivos que serão utilizados.
-- A rotina para a execução periódica foi implementada utilizando o Windows Task Scheduler e está no arquivo Pipeline_Coleta_CNPJ.xml.
-- As bibliotecas necessárias para a execução do código estão no arquivo requirements.txt
