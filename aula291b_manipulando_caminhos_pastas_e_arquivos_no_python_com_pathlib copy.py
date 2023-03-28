import os
from pathlib import Path

# pathlib trabalha com caminhos

caminho_projeto = Path()
print(caminho_projeto)  # caminho relativo
# print(caminho_projeto.absolute())  # caminho absoluto

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)

caminho = os.path.join("/Users", "iurim", "OneDrive",
                       "Área de Trabalho", "pasta_teste")
# print(caminho)

ideias = caminho_arquivo.parent / "ideias"

print(ideias)
print(ideias / 'arquivo.txt')
print(Path.home())
print(Path.home() / 'Área de Trabalho')

# # caminho do arquivo
# arquivo = Path.home() / "OneDrive" / "Área de Trabalho" / "arquivo.txt"

# # criando o arquivo
# arquivo.touch()
# print(arquivo)

# arquivo.write_text('Olá Mundo')
# print(arquivo.read_text())

# # apagando o arquivo
# # arquivo.unlink()
