from pathlib import Path

caminho_pasta = Path.home()/"OneDrive"/"Área de Trabalho"/"Python e legal"

files = caminho_pasta / "files"
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f"file_{i}.txt"

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá Mundo!\n')
        text_file.write(f'file_{i}.txt')
# função recursiva para apagar as pastas e arquivos
# de dentro pra fora

# rmtree(caminho_pasta)
