class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Cliente(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.tipo = "Cliente"

class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.tipo = "Administrador"