# Classe = Molde(geralmente sem dados)
# Instancia da classe(objeto) = Tem dados
# Uma classe pode gerar varias instancias
# Na classe, o self é a propria instancia

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar