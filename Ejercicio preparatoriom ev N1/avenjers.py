avengers = []
while True:
    print(f"1)agregar \n2)visualizar/modificar \n3)salir")
    seleccion = input("seleccione su opcion")
    largo_avng = len(avengers)
    if seleccion == "1":
        heroe_ingresado = input("ingrese el nombre del heroe")
        avengers.append(heroe_ingresado)
    elif seleccion == "2":
        indice = 0
        for heroe in avengers:
            print(f"vengador: {indice}-{heroe}")
            indice += 1
        seleccion_modificacion = input("desea modificar la lista? y/n")
        if seleccion_modificacion == "y":
            for i in range(len(avengers)):
                avengers[i] = avengers[i].upper()
    elif seleccion == "3":
        break
    elif seleccion == "SACRIFICAR":
        print(f"c mato el {avengers[-1]}")
        avengers.pop()