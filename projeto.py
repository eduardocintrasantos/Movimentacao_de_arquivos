import os
import shutil
import time

# Diretório de Origem 
diretorio_origem = "./relatorios"

# Diretório de Destino
diretorio_destino = "./relatorios processados"

# Verifica se existe a pasta de destino, e se não existir irá criar
if not os.path.exists(diretorio_destino):
    os.mkdir(diretorio_destino)

# Lista todos os arquivos do diretorio de Origem 
arquivos = os.listdir(diretorio_origem)

# Criado um dicionario para guardar as informações sobre os arquivos que existem
info_arquivos = {}

# Opção usando for para consultar os arquivos que contem '_processado' na descrição
for arquivos in os.listdir(diretorio_origem):
    if '_processado' in arquivos:
        print(arquivos)

# Conulsar os arquivos que contem '_processado' utilizando list comprehension
arquivos_processados = [arquivo for arquivo in arquivos if arquivo.endswith('_processado.xlsx')]
print(arquivos_processados)