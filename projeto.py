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
# for arquivos in os.listdir(diretorio_origem):
#    if '_processado' in arquivos:
#        print(arquivos)

# Conulsar os arquivos que contem '_processado' utilizando list comprehension
arquivos_processados = [arquivo for arquivo in arquivos if arquivo.endswith('_processado.xlsx')]
print(arquivos_processados)

# Pegar cada arquivo processado e mover para a pasta 'relatorios processados'
for arquivo_processado in arquivos_processados:
    caminho_completo_origem = os.path.join(diretorio_origem, arquivo_processado)
    caminho_completo_destino = os.path.join(diretorio_destino, arquivo_processado)

    shutil.move(caminho_completo_origem, caminho_completo_destino)

    print(f'Arquivo {caminho_completo_origem} movido para {caminho_completo_destino}')

# Adicionando informações adicionais sobre os arquivos movidos
for arquivo in arquivos_processados:
    caminho_completo = os.path.join(diretorio_destino, arquivo)

    # Salvando as informações de tamanho e data criação dos arquivos movidos 
    tamanho = os.path.getsize(caminho_completo)
    data_criacao = time.ctime(os.path.getctime(caminho_completo))

    # Adicionando as informações ao dicionario criado
    info_arquivos[arquivo] = [tamanho, data_criacao]

print(info_arquivos)
print(f'Quantidade de arquivos movidos: {len(info_arquivos.keys())}')