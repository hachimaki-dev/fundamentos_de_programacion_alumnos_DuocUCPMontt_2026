vengadores = []

while True:
    print("1. Agregar Avenger")
    print("2. Mostrar Base")
    print("3. Salir")
    opcion = input("Seleccione una opción (Del 1 al 3)").upper()
    if opcion == "1":
        vengadores.append(input("Ingrese el nombre de su vengador").upper())
    elif opcion == "2":
        contador = 0
        for vengador in vengadores:
            print(f"Averger {contador} = {vengador}")
            contador + 1
    elif opcion == "3":
        print("Saliendo del programa")
        break
    elif opcion == "SACRIFICAR":
        print("Sacrificando al ultimo avenger agregado")
        vengadores.pop()
    else:
        print("Escoja una opción valida")
print(f"Su lista de vengadores es: {vengadores}")