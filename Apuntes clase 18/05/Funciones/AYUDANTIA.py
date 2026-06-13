inventario_minimarket = []
#FUNCION DE CREACION DE PRODUCTOS
def crear_producto(nombre, precio, stock, categoría):
    producto = {"nombre": nombre, "precio": precio, "stock": stock, "categoría": categoría}
    return producto

#FUNCION DE BUSQUEDA
def buscar_producto(inventario, nombre_buscador):
    for i in range(len(inventario)):
        if inventario[i]["nombre"].lower() == nombre_buscador.lower():
            return i
    return -1 # 0 = arroz 1 = atun  2 = pollo  -1 = NADA

#REABASTECER PRODUCTO (SIN RETURN)
def reabastecer_producto(inventario, nombre_buscado, cantidad):
    posicion = buscar_producto(inventario, nombre_buscado)
    if posicion != -1:
        inventario[posicion]["stock"] += cantidad
        print(f"Stock actualizado a : {inventario[posicion]["stock"]}")
    else:
        print("El producto no fue encontrado")

def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("\nEl inventario está vacío.")
    else:
        print(" === Lista de productos ===")
        for prod in inventario:
            print(f"Producto: {prod["nombre"]} | Precio: ${prod["precio"]}  \nStock: {prod["stock"]} | Categoría: {prod["categoría"]}")
print("=== BIENVENIDO AL MINIMARKET DE DON TITO ===")
while True:
    while True:
        print("\/\/\ MENÚ /\/\/")
        eleccion_usuario = input("1. Registrar nuevo producto\n2. Reabastecer productos\n3. Mostrar inventario\n4. Buscar producto\n5. Salir")
        if eleccion_usuario in ["1", "2", "3", "4", "5"]:
                break
        else:
            print("Ingrese una opción correcta.")

    if eleccion_usuario == "1":
        print("== Registra un nuevo producto ==")
        #VALIDACIÓN DEL NOMBRE
        while True:
            nombreprod = input("Nombre del producto: ").strip()
            if nombreprod != "":
                break
            print("Error, no puedes ingresar un nombre vacío.")
        #VALIDACIÓN DE PRECIO
        while True:
            precio_str = input("Precio: ")
            if precio_str.isdigit() and int(precio_str) > 0:
                pre = int(precio_str)
                break
            print("Error, el precio debe ser mayor a 0.")
        #VALIDACIÓN DE STOCK
        while True:
            try: 
                stock_inicial = int(input("Stock inicial: "))
                if stock_inicial > 0:
                    print(f"Stock inicial: {stock_inicial}")
                    break
                else:
                    print("Error, debes ingresar un número entero positivo.")
            except ValueError:
                print("Error, debe ingresar numeros enteros positivos.")
        categor = input("Categoría: ")
        #CREACION DIRECTA
        nuevo_producto = crear_producto(nombreprod, precio_str, stock_inicial, categor)
        inventario_minimarket.append(nuevo_producto)
        print(f"{nombreprod} Agregado al inventario.")

    elif eleccion_usuario == "2":
        nombreprod = input("¿Que producto desea reabastecer? ").strip()
        while True:
            try:
                cantidad_a_reabastecer = int(input("¿Cuantas unidades se agregarán? "))
                if cantidad_a_reabastecer > 0:
                    reabastecer_producto(inventario_minimarket, nombreprod, cantidad_a_reabastecer)
                    break
                else:
                    print("ERROR, debe ingresar un número entero positivo.")
            except ValueError:
                print("ERROR, debe ingresar un número entero positivo.")
    elif eleccion_usuario == "3":
        mostrar_inventario(inventario_minimarket)
    elif eleccion_usuario == "4":
            busqueda_prod = input("¿Qué producto desea buscar? ").strip()
            if busqueda_prod.lower() in inventario_minimarket["nombre"].lower():    #REVISAR
                buscar_producto(inventario_minimarket, busqueda_prod)
    else:
        print("Has salido del minimarket, hasta la próxima.")
        break