from clases.producto import Producto
from clases.carrito import Carrito
from clases.usuario import Usuario, Cliente, Administrador

print("¡Bienvenido a la Tienda Virtual en Consola!")

mi_carrito = Carrito()

# Creando una lista con el catálogo de productos disponible
catalogo_productos = [
    Producto("Televisor", 1200000, 5),
    Producto("Celular", 800000, 10),
    Producto("Audífonos", 150000, 15),
    Producto("Computador", 2500000, 3)
]

continuar = True
while continuar == True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver catálogo de productos")
    print("2. Agregar producto al carrito")
    print("3. Ver mi carrito de compras")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        print("\n--- CATÁLOGO DE PRODUCTOS ---")
        # Usamos un ciclo para mostrar cada producto del catálogo con su número
        posicion = 1
        for prod in catalogo_productos:
            print(str(posicion) + ". " + prod.nombre + " - Precio: $" + str(prod.obtener_precio()) + " - Stock: " + str(prod.obtener_stock()))
            posicion = posicion + 1
            
    elif opcion == "2":
        # Dejamos esto simple por ahora, lo mejoraremos en la siguiente rama
        print("\nFunción para agregar (se mejorará en la siguiente rama)")
            
    elif opcion == "3":
        mi_carrito.ver_carrito()
        
    elif opcion == "4":
        print("Gracias por usar la tienda. ¡Adiós!")
        continuar = False