# O professor fala que em python este metodo é praticamente inutil
# Métodos estaticos são metodos que estão dentro da classe
# em resumo, são funções que existem denro da sua classe

class Classe:
    @staticmethod
    def fucao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)
    
def fucao(*args, **kwargs):
        print('Oi', args, kwargs)


c1 = Classe()
c1.fucao_que_esta_na_classe(1, 2, 3)
c1.funcao(1, 2, 3)
Classe.fucao_que_esta_na_classe(nomeado=1)
c1.funcao(nomeado=1)