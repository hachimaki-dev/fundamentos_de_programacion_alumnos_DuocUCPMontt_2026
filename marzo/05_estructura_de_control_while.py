condicion = True

while condicion == True:
    print("Bienvenido, elija una opción")
    print("1. Contar chiste")
    print("2. Contar adivinanza")
    print("3. Salir")

    opcion_elegida = int(input("Elija su opción: "))

    if opcion_elegida == 1:
        print("\nAquí se mostrarán los chistes\n")
    elif opcion_elegida == 2:
        print("\nAquí se mostrarán las adivinanzas\n")
    elif opcion_elegida == 3:
        condicion = False
    else:
        print("Opción inválida")

print("\nFin del programa")
