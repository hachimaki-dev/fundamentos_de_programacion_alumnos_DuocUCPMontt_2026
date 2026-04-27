vengadores = []
while True:
    print("1.Agregar héroe\n2.Mostrar base y Modificar\n3.Salir")
    accion = int(input("Ingrese su opción : \n"))
    if accion == 1:
        nombre_heroe = input("Ingrese el nombre del heroe : ")
        vengadores.append(nombre_heroe)
    elif accion == 2:
        for i in range(len(vengadores)):
            print(f"")