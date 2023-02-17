# meethod vs @classmethod vs @staticmethod
# method - self, metodo de instancia
# @classmethod - cls, metodo de classe
# @staticmethod - metodo estatico (xself, cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        return connection
    

c1 = Connection.create_with_auth('luiz', '1234')
print(c1.user)
print(c1.password)

