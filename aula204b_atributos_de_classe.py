# Atributos de classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Tainá', 35)
p2 = Pessoa('Iuri', 37)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
