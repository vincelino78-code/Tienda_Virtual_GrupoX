# Clase Carrito de compras
class Carrito:
    def __init__(self):
        self.items = []
    def agregar_producto(self, producto):
        self.items.append(producto)
