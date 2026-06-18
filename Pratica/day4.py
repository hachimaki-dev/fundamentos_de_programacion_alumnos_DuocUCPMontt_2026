inventario_minimarket = []

def crear_productos(nombre, precio, stock, categoria):
    producto = {
        "nombre:" : nombre,
        "precio:" : precio,
        "stock:" : stock,
        "categoria:": categoria
    }
    return producto

def buscar_producto(inventario, nombre_buscado):
    for i in range(len(inventario)):
        if inventario(i)("nombre:").lower() == nombre_buscado.lower():
            return i
        return -1

def reabastecer_producto(inventario, nombre_buscado, cantidad):
    posicion = buscar_producto(inventario, nombre_buscado)
    if posicion != -1:
        inventario[posicion]["strack"] += cantidad
        print(f"Stock actualizado con exito, el nuevo stock es: {inventario[posicion ['stack']]}") 
    else:
        print("producto no encontrado")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        print("\n=== Lista de productos ===")
        for prod in inventario:
            print(f"Producto: {prod['nombre']} | Precio $: {prod['precio $']} | Strock: {prod['strock']} unidades | Categoria: {prod['categoria']}")

while True:
    print("\n-------- MINIMARKET DON TITO --------")
    print("----------- Menú principal -----------")
    print("Opcion 1. Registrar nuevo producto")
    print("Opcion 2. Reabastecer stock")
    print("Opcion 3. Ver inventario completo")
    print("Opcion 4. Salir")
    print("-------------------------------------")
    
    opcion = input("Selecciona la opcion que deseas (1 a 4): ")
    
    if opcion == "1":
        print("--- REGISTRAR PRODUCTO ---")
        while True:
            nombre_producto = input("Nombre del producto: ").strip()
            if nombre_producto != "":
                break
            print("Error el nombre no puede estrar vacio")
        while True:
            precio_str = input("Precio: ")
            if precio_str.isdigit() and int(precio_str) > 0:
                precio = int(precio_str)
                break
            print("Error precio debe ser mayor a 0")
        while True:
            stock_str = input("Stock inicial: ")
            if stock_str.isdigit() and int(stock_str) > 0:
                stock = int(stock_str)
                break
            print("Error: El stock debe ser un número mayor a 0")

        categoria = input("Categoria: ")

        nuevo = crear_producto(nombre_producto, precio_str, stock_str)
        inventario_minimarket.