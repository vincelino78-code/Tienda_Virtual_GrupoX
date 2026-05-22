class Carrito:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print("Producto agregado al carrito con éxito.")

    def ver_carrito(self):
        if len(self.lista_productos) == 0:
            print("Tu carrito está vacío.")
        else:
            print("--- Productos en tu Carrito ---")
            for prod in self.lista_productos:
                print("- " + prod.nombre + " ($" + str(prod.obtener_precio()) + ")")