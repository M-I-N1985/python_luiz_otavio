from pathlib import Path

caminho_arquivo = Path.home() / "OneDrive" / "Área de Trabalho" / "arquivo.txt"
caminho_arquivo.touch()
caminho_arquivo.write_text("")

with caminho_arquivo .open('a+') as file:
    file.write('Uma linha\n')
    file.write('Outra linha\n')

print(caminho_arquivo.read_text())

# apagando o arquivo
# caminho_arquivo.unlink()
