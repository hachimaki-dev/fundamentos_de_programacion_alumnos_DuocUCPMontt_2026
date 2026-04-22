vengadores= []
while True:
    print("\nMenu de opciones")
    print("1. agregar avenger")
    print("2. Mostrar base")
    print("3. salir")
    opcion_elegida= int(input("Elige una opcion (1/2/3): "))

    if opcion_elegida == 1:
        nombre_heroe= input("Ingresa el nombre de el heroe: ")
        vengadores.append(nombre_heroe)
    elif opcion_elegida == 2:
        for i in range(len(vengadores)):
            vengadores[i]= vengadores[i].upper()
            print(f"\n{vengadores}")
    elif opcion_elegida == 4:
        vengador_sacrificado= input("Ingresa el vengador a sacrificar")
        vengador_sacrificado= [i].pop
    else:
        break