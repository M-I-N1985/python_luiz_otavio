# class - Classes são moldes para criar novo objetos
# As classes geram novos objetos (instâncias) que 
# podem ster seus proprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.
# string = 'Luiz' # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Iuri'
p1.sobrenome = 'Mesquita'

p2 = Pessoa()
p2.nome = 'Tainá'
p2.sobrenome = 'Vianna'

print(p1.nome)
print(p1.sobrenome)
