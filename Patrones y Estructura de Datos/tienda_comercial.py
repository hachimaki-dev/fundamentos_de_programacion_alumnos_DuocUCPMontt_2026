datos_tienda = []


while True:
    try:
        registrar_productos = int(input("Ingrese cuantos Productos se Van a Registrar :     "))
        if registrar_productos <= 0:
            print("Ingrese un numero entero positivo")
        else:
            break
    except ValueError:
        print("Ingrese una opcion valida")

for p in range(registrar_productos):

    while True:

        nombre_producto = input("Ingrese el Nombre del Producto :   ")
        if len(nombre_producto) < 3 or " " in nombre_producto:
            print("Ingrese un nombre con un minimo de 3 caracteres y sin espacios")
        else:
            break
    
    
    while True:
        try:
            precio_producto = int(input("Coloque el Precio del Producto :   "))
            if precio_producto <= 0:
                print("Ingrese un numero entero positivo ")
            else:
                break
        except ValueError:
            print("Ingrese una opcion valida")


    datos_producto = {"nombre": nombre_producto , "Precio" : precio_producto}
    datos_tienda.append(datos_producto)


print("==="*8)
print("Registro de Productos")
print("==="*8)
print()
for x in datos_tienda:
    
    print(f"Producto : {x["nombre"]} | Precio : {x["Precio"]}")

