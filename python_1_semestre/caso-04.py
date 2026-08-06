
inventario_minimarket= []
def crear_producto(nombre, precio, stock, categoria):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria
    }
    return producto
#Funcion de busqueda
def buscar_producto(inventario, nombre_buscado):
    for i in range(len(inventario)):
        
        if inventario [i]["nombre"].lower() == nombre_buscado.lower():
            return i
        return -1
def reabastecer_producto(inventario, nombre_buscado, cantidad):
    posicion = buscar_producto(inventario, nombre_buscado)
    if posicion != -1:
        inventario[posicion]["stock"] += cantidad
        print(f'Stock actualizado con exito, el nuevo stock es: {inventario[posicion ['stock']]}')
    else:
        print("producto no encontrado")
        
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        print("\n=== Lista de productos ===")
        for prod in inventario:
            print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Stock: {prod['stock']} unidades | Categoria: {prod['categoria']}")

while True:
    print("\n--- MINIMARKET DON TITO ---\n1. Registrar nuevo producto\n2. Reabastecer stock\n3. Ver inventario completo\n4. Salir")
    opcion = input("Seleccione una opcion")

    if opcion == "1":
        print("--- REGISTRAR PRODUCTO ---")
        while True:
            nom = input("Nombre del producto: ").strip()
            if nom != "":
                break
            print("Error el nombre no puede estar vacio")
        while True:
            pre_str = input("Precio: ")
            if pre_str.isdigit() and int(pre_str) > 0:
                pre = int(pre_str)
                break
            print("error precio debe ser mayor a 0")
        while True:
            stk_str = input("Stock inicial: ")
            if stk_str.isdigit() and int(stk_str) > 0:
                stk = int(stk_str)
                break
            print("Error: El stock debe ser un número mayor a 0.")
            
        cat = input("Categoría: ")

        nuevo = crear_producto(nom, pre, stk, cat)
        inventario_minimarket.append(nuevo)
        print(f'{nom} agregado con exito al inventario')
    elif opcion == "2":
        print("\n--- REABASTECER STOCK ---")
        nom = input("¿Qué producto desea reabastecer?: ")
        cant_str = input("¿Cuántas unidades llegan?: ")
        if cant_str.isdigit() and int(cant_str) > 0:
            reabastecer_producto(inventario_minimarket, nom, int(cant_str))
        else:
            print("Cantidad inválida.")
    elif opcion == "3":
        mostrar_inventario(inventario_minimarket)
    elif opcion == "4":
        print("Adios don tito")
        break
    else:
        print("opcion no valida intent otra vez")