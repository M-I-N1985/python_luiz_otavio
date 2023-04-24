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
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('Log', msg)
    

c1 = Connection.create_with_auth('luiz', '1234')
print(Connection.log('Essa é a msg de log'))
print(c1.user)


