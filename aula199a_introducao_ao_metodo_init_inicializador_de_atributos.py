# Preste atencao como o inicializador faz a mesma funcao que 
# as instancias abaixo. Onde na aula anterior ele atribuia
# p1.nome = luiz, com o construtor ele atribui a instancia ao self
# e ao invez de atribuir nomes diretamente, agora ele atribui
# dentro do construtor
 

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa()
#p1.nome = 'Iuri'
#p1.sobrenome = 'Mesquita'

p2 = Pessoa()
#p2.nome = 'Tainá'
#p2.sobrenome = 'Vianna'

print(p1.nome)
print(p1.sobrenome)
