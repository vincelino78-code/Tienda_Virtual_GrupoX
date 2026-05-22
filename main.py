from clases.producto import Producto
from clases.carrito import Carrito
from clases.usuario import Usuario, Cliente, Administrador

print("¡Bienvenido a la Tienda Virtual en Consola!")

mi_carrito = Carrito()
tele = Producto("Televisor", 1200000, 5)
celular = Producto("Celular", 800000, 10)

continuar = True
while continuar == True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver productos disponibles")
    print("2. Agregar producto al carrito")
    print("3. Ver mi carrito de compras")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        print("\nProductos en la tienda:")
        print("1. " + tele.nombre + " - Precio: $" + str(tele.obtener_precio()) + " - Stock: " + str(tele.obtener_stock()))
        print("2. " + celular.nombre + " - Precio: $" + str(celular.obtener_precio()) + " - Stock: " + str(celular.obtener_stock()))
        
    elif opcion == "2":
        print("\n¿Qué producto quieres agregar?")
        print("1. " + tele.nombre)
        print("2. " + celular.nombre)
        elegido = input("Selecciona 1 o 2: ")
        if elegido == "1":
            mi_carrito.agregar_producto(tele)
        elif elegido == "2":
            mi_carrito.agregar_producto(celular)
        else:
            print("Opción no válida.")
            
    elif opcion == "3":
        mi_carrito.ver_carrito()
        
    elif opcion == "4":
        print("Gracias por usar la tienda. ¡Adiós!")
        continuar = False
        
    else:
        print("Opción incorrecta, intenta de nuevo.")