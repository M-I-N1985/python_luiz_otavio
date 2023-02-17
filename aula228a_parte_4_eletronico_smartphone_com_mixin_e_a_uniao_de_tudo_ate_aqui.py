# Está incompleto pois ficou faltando modulos das outras partes
# --------------COMPLETAR---------------

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self.ligado = True
    
    # Observe que não tem um return no final, isso se chama return early.
    def desligar(self):
        if self.ligado:
            self.ligado = False


class smartphone(Eletronico):
    ...
