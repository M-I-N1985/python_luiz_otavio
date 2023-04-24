from pathlib import Path

# def rmtree(root: Path, remove_root=True):
#     # para algum aquivo especifico poderiamos usar ('**/*.txt')
#     for file in root.glob('*'):
#         if file.is_dir():
#             print('DIR: ', file)
#             rmtree(file, False)
#             file.rmdir()
#         else:
#             print('FILE: ', file)
#             file.unlink()

#     if remove_root:
#         root.rmdir()


caminho_pasta = Path.home()/"OneDrive"/"Área de Trabalho"/"Python e legal"
print(caminho_pasta)

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


# rmtree(caminho_pasta)
