productos = [
    {"nombre": "Arroz", "stock": 50},
    {"nombre": "Aceite", "stock": 20},
    {"nombre": "Harina", "stock": 35}
]

productos_encontrado = False

while True:
    print("\n=== GESTIÓN DE PRODUCTOS ===")
    print("1. Ver todos los Productos \n2. Actualizar stock \n3. Eliminar un Producto \n4. Salir ")
    print()
    
    try:
        opcion_a_elegir = int(input("Ingrese la opcion a Realizar :     "))
        if opcion_a_elegir <= 0 or opcion_a_elegir > 4:
            print("ingrese una opcion valida   ")
        elif opcion_a_elegir == 4:
            print("Saliendo del panel de gestión.")
            print()
            print("Productos y Sus Stock finales")
            for i in productos:
                print(f"Nombre : {i["nombre"]} | Stock : {i["stock"]} ")
            break
        elif opcion_a_elegir == 1:
            for i in productos:
                print(f"Nombre : {i["nombre"]} | Stock : {i["stock"]} ")
            print()
        elif opcion_a_elegir == 2:
            
            nombre_actualizar = input("Ingrese el nombre del Producto a Actualizar Stock :      ").lower()
            productos_encontrado = False
            for i, p in enumerate(productos):
                if p["nombre"].lower() == nombre_actualizar.lower() :
                    while True:
                        try:
                            stock_nuevo = int(input(f"Ingrese el nuevo valor de stock de {p['nombre']} :    "))
                            if stock_nuevo <= 0:
                                print("Ingrese un numero entero positivo ")
                            else:
                                productos[i]["stock"] = stock_nuevo
                                print("Se a Actualizado el Stock")
                                productos_encontrado = True
                                break
                        except ValueError:
                            print("ingrese una opcion valida")
            if not productos_encontrado:
                print("Producto no encontrado")
        elif opcion_a_elegir == 3:
            eliminar_producto = input("Ingrese el nombre del Producto a Eliminar :  ")
            productos_encontrado = False
            for i, p in enumerate(productos):
                if p["nombre"].lower() == eliminar_producto.lower():
                    eliminado = productos.pop(i)
                    print(f"Se a eliminado el Producto {eliminado['nombre']} exitosamente.")
                    productos_encontrado= True
                    break
            if not productos_encontrado:
                print("Producto no Encontrado")
    except ValueError:
        print("Ingrese una opcion valida")
        