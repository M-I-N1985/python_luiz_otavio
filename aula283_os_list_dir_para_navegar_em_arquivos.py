# os.listdir para navegar em caminhos
# /Users/iurim/OneDrive/Área de Trabalho/Documentos pessoais e fotos/Certificados - no mac ou linux
# C:\Users\iurim\OneDrive\Área de Trabalho\Documentos pessoais e fotos\Certificados - no windows

import os

# caminho = r'C:\\Users\\iurim\\OneDrive\\Área de Trabalho\\Documentos pessoais e fotos\\Certificados'  # no windows
# print(caminho)

caminho = os.path.join('/Users', 'iurim', 'OneDrive', 'Área de Trabalho', 'Documentos pessoais e fotos', 'Certificados')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)