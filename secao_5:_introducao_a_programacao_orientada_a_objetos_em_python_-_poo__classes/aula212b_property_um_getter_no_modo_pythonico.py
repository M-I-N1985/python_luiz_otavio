# @property - um getter no modo Pythônico
# getter - um metodo para obter um atributo
# @property é uma propriedade do objeto, ela é um metodo que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código clientes - é o ódigo que usa seu código

class Caneta:
    def __init__(self, cor):
        self.cor = cor
    
    def get_cor(self):
        return self.cor

###############################

# Se em algum momento vc precisar modificar o atributo cor, como fazer para 
# nao interfereir no objeto que a equipe esta usando?
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)
caneta = Caneta('Azul')
print(caneta.cor)