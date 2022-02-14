from data_extract import download_files
from transform_1 import data_standardization
from transform_2 import data_conformation
from save_data_to_db import save_file_to_db

###########################################################
################## Download dos arquivos ##################
print("Iniciando o download dos arquivos para a pasta Raw")
## Links
dados_empresa = "http://200.152.38.155/CNPJ/K3241.K03200Y0.D20108.EMPRECSV.zip"
dados_estabelecimento = "http://200.152.38.155/CNPJ/K3241.K03200Y0.D20108.ESTABELE.zip"
dados_socios = "http://200.152.38.155/CNPJ/K3241.K03200Y0.D20108.SOCIOCSV.zip"
## Chama as funções para realizar o download
download_files(dados_empresa, "empresa.zip", "raw")
download_files(dados_estabelecimento, "estabelecimento.zip", "raw")
download_files(dados_socios, "socios.zip", "raw")
print("Fim o download dos arquivos para a pasta Raw")

############################################################
################ Padronização dos arquivos ################# 
print("Iniciando a padronização dos arquivos para a pasta standardized")
## Define os arquivos que serão convertidos e em que pasta estão
files_to_convert = ["socios.zip", "empresa.zip", "estabelecimento.zip"]
directory_to_open = "raw"

## Define o nome dos arquivos convertidos e a pasta em que estarão
files_to_save = ["socios.csv", "empresa.csv", "estabelecimento.csv"]
directory_to_save = "standardized"

## Chama a função de padronização para cada um dos arquivos
for i in range(0, 3):
    data_standardization(directory_to_open, files_to_convert[i], directory_to_save, files_to_save[i])
print("Fim da padronização dos arquivos para a pasta standardized")

#############################################################
################ Conformização dos arquivos #################
print("Iniciando a conformização dos dados para a pasta conformed")
## Define os arquivos que serão conformados e em que pasta estão
files_to_prepare = ["empresa.csv", "socios.csv", "estabelecimento.csv", ]
directory_to_open = "standardized"

## Define o nome dos arquivos conformados e a pasta em que estarão
files_to_save = ["empresa.csv", "socios.csv", "estabelecimento.csv", ]
directory_to_save = "conformed"

for i in range(0, 3):
    data_conformation(directory_to_open, files_to_prepare[i], directory_to_save, files_to_save[i])
print("Fim da conformização dos dados para a pasta conformed")

###############################################################################
################ Salvamento dos dados no banco de dados MySql #################

files_to_save = ['empresa.csv', 'socios.csv', 'estabelecimento.csv']
directory_files = 'conformed'

save_file_to_db(files_to_save, directory_files)   





