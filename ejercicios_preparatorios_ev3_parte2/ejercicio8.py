while True:
    try:
        cantidad_productos = int(input("¿Cuantos productos desea registrar?: "))
        if cantidad_productos > 0:
            break
        print("Solo se permiten numeros positivos.")
    except ValueError:
        print("Dato invalido: Ingrese un numero positivo")

inventario = []

for i in range(cantidad_productos):
    print(f"Producto numero {i+1}.")
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").strip()
        if len(nombre_producto) >= 3:
            break
        print("Nombre inválido. Mínimo 3 caracteres y sin espacios (usa una sola palabra).")
    
    while True:
        try:
            precio_producto = int(input("Ingrese el precio del producto: "))
            if precio_producto > 0:
                break
            print("Solo se permiten numeros positivos.")
        except ValueError:
            print("Dato invalido: Ingrese un numero positivo")
    
    producto = {"nombre": nombre_producto, "precio": precio_producto}
    inventario.append(producto)

print("---- RESUMEN COMPRA ----")
for producto in inventario:
    print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]}")