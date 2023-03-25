# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
print(HOME)
DESKTOP = os.path.join(HOME, 'OneDrive', 'Área de Trabalho')
print(DESKTOP)
PASTA_ORIGINAL = os.path.join(DESKTOP, 'pasta_teste')
print(PASTA_ORIGINAL)
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
print(NOVA_PASTA)
print( )

os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for file in files:
#         print(file)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)