# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'OneDrive', 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'pasta_teste')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

# os.link não funciona, pois essa exlcusão tem que ser recursiva, ou seja, apagar as pastas internas e indo arquivo por arquivo, até apagar a apasta
# os.unlink(NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)  # 
# hutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)  # copia a pasta e cola na nova
# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
