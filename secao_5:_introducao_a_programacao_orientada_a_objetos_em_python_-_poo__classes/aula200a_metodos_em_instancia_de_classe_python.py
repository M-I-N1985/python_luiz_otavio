# Método em instância de classe python
class Carro:
    def __init__(self):
        self.nome = 'Fusca' # Hard coded
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro()
print(fusca.nome)
fusca.acelerar()

celta = Carro()
print(celta.nome)
celta.acelerar()
