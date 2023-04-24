# Método de classe (@classmethod) + factories methods (métodos fábrica)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro
# parâmetro recebermos nossa própria classe

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')


p1 = Pessoa('João', 34)
print(Pessoa.ano)
Pessoa.metodo_de_classe()