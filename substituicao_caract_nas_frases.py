
frase = input("Digite a frase: ")
# frase = "3. Inção às"
frase = frase.lower().split()  # type: ignore
nova_frase = ""
nova_palavra = ""

for palavra in frase:
    for letra in palavra:
        if letra in ['á', 'à', 'ã', 'â']:
            letra = 'a'
            nova_palavra = nova_palavra + letra
        elif letra in ['é', 'ê']:
            letra = 'e'
            nova_palavra = nova_palavra + letra
        elif letra == 'í':
            letra = 'i'
            nova_palavra = nova_palavra + letra
        elif letra in ['ó', 'ô', 'õ']:
            letra = 'o'
            nova_palavra = nova_palavra + letra
        elif letra == 'ú':
            letra = 'u'
            nova_palavra = nova_palavra + letra
        elif letra == 'ç':
            letra = 'c'
            nova_palavra = nova_palavra + letra
        elif letra in "(":
            letra = '_'
            nova_palavra = nova_palavra + letra
        elif letra in ')':
            letra = '_'
            nova_palavra = nova_palavra + letra
        elif letra in ' ':
            letra = '_'
            nova_palavra = nova_palavra + letra
        elif letra in '.':
            letra = '_'
            nova_palavra = nova_palavra + letra
        elif letra in ",":
            letra = '_'
            nova_palavra = nova_palavra + letra

        else:
            nova_palavra = nova_palavra + letra

    nova_palavra = nova_palavra + "_"

nova_frase = 'aula' + nova_palavra
nova_frase = nova_frase[:-1] + ".py"
print(nova_frase)
