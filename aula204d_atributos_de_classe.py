# Atributos de classe

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100  # Aqui ele colocou como atrib. de instancia para mostrar como
                              # o interpretador faz a busca na instancia primeiro, depois na classe


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('Tainá', 35)
p2 = Pessoa('Iuri', 37)
print(p1.get_ano_nascimento())  # Foi um erro proposital
