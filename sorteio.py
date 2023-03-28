import random

# números que saíram nos últimos 3 e 4 sorteios
ultimos_3_sorteios = [8, 12, 25]
ultimos_4_sorteios = [8, 12, 22, 25]

# números que apareceram menos e mais nos últimos 6 sorteios
menos_6_sorteios = [3, 6, 13]
mais_6_sorteios = [2, 4, 8, 10, 11, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23]

# frequência de ocorrência de cada número
frequencia = {1: 22, 2: 18, 3: 15, 4: 15, 5: 12, 6: 13, 7: 10, 8: 15, 9: 9, 10: 12,
              11: 12, 12: 14, 13: 10, 14: 12, 15: 8, 16: 10, 17: 11, 18: 10, 19: 10,
              20: 11, 21: 10, 22: 12, 23: 12, 24: 9, 25: 10}

# lista para armazenar as sequências geradas
sequencias = []

# gerar 15 sequências
for i in range(15):
    sequencia = []

    # adicionar os números que apareceram menos nos últimos 6 sorteios
    for num in menos_6_sorteios:
        if num not in sequencia:
            sequencia.append(num)

    # preencher com os outros números, de acordo com a frequência de ocorrência e as condições impostas
    while len(sequencia) < 15:

        # escolher um número aleatório, ponderando de acordo com a frequência de ocorrência
        num = random.choices(range(1, 26), weights=[
                             frequencia[n] for n in range(1, 26)])[0]

        # verificar se o número não está nos últimos 3 ou 4 sorteios
        if num not in ultimos_3_sorteios and num not in ultimos
