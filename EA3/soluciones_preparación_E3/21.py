capacidad_maquina = 20
mesas_disponibles = 20
print("bienvenido al sistema de gestion de mesas del restaurante")

while True:
    print("mesas disponibles:")
    print("asignar mesas")
    print("liberar mesas")
    print("mesas ocupadas")
    print("salir")

    opcion = input("ingrese una opcion, del 1 al 5: ")

    if opcion == "1":
        print("mesas disponibles: ", mesas_disponibles)
    elif opcion == "2":
        cantidad = int(input("¿cuantas mesas desea asignar? "))
        if cantidad <= mesas_disponibles:
            mesas_disponibles -= cantidad
            print("mesas asignadas: ", cantidad)
            print("mesas disponibles: ", mesas_disponibles)
        else:
            print("no hay suficientes mesas disponibles")
    elif opcion == "3":
        cantidad = int(input("¿cuantas mesas desea liberar? "))
        if cantidad <= (capacidad_maquina - mesas_disponibles):
            mesas_disponibles += cantidad
            print("mesas liberadas: ", cantidad)
            print("mesas disponibles: ", mesas_disponibles)
        else:
            print("no hay suficientes mesas ocupadas para liberar")
    elif opcion == "4":
        print("mesas ocupadas actualmente: ", capacidad_maquina - mesas_disponibles)
    elif opcion == "5":
        print("servicio terminado! Buenas noches")
        break
    else:
        print("opcion no valida, por favor ingrese una opcion del 1 al 5") 

