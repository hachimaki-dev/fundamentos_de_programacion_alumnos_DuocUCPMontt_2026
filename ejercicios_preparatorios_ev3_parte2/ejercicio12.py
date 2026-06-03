productos = [{"nombre": "Arroz", "stock": 50},
            {"nombre": "Aceite", "stock": 20},
            {"nombre": "Harina", "stock": 35}]

while True:
    print("\n=== GESTIÓN DE PRODUCTOS ===")
    print("1. Ver todos los productos")
    print("2. Actualizar stock de un producto")
    print("3. Eliminar un producto")
    print("4. Salir")

    opcion_elegida = int(input("Seleccion una opcion (1-4): "))

    if opcion_elegida == 1:
        print("------ Productos en stock ------")
        for producto in productos:
            print(f"Nombre: {producto['nombre']} | Stock: {producto['stock']}")

    elif opcion_elegida == 2:
        nombre_producto = input("¿Que producto desea buscar?: ").strip()
        encontrado = False
        for i, producto in enumerate(productos):
            if producto["nombre"].lower() == nombre_producto.lower():
                while True:
                    try:
                        nuevo_stock = int(input(f"Nuevo stock para {producto["nombre"]}: "))
                        if nuevo_stock >= 0:
                            productos[i]["stock"] = nuevo_stock
                            print("Se ha actualizado exitosamente.")
                            encontrado = True
                            break
                        print("El stock debe ser 0 o mayor.")
                    except ValueError:
                        print("Ingresa un entero válido.")
                break
        if not encontrado:
            print("Producto no encontrado")
    
    elif opcion_elegida == 3:
        nombre_producto = input("¿Que producto desea eliminar?: ").strip()
        encontrado = False
        for i, producto in enumerate(productos):
            if producto["nombre"].lower() == nombre_producto.lower():
                producto_eliminado = productos.pop(i)
                print(f"Producto {producto_eliminado["nombre"]} eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    
    elif opcion_elegida == 4:
        print("Saliendo del sistema.")
        break
    
    else:
        print("Solo se puede seleccionar desde 1 al 4.")