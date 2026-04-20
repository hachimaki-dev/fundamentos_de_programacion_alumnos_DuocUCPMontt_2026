# vengadores = []
vengadores = ["Iron Man", "Thor", "Capitán America", "Hulk"]

print("/" * 32)
print("BASE DE LOS AVENGERS")
print("/" * 32)

while True:
    print("\n1. Agregar Avenger    2. Mostrar Base y Modificar    3. Salir")
    eleccion = input("Ingrese una opción: ")
    eleccion = eleccion.lower()

    if eleccion == "1":
        nombre_heroe = input("Nombre del héroe a agregar: ")
        vengadores.append(nombre_heroe)

    elif eleccion == "2":
        for i in range(len(vengadores)):
            print(f"{i} - {vengadores[i]}")

        eleccion_mayusculas = input('¿Quieres cambiar el nombre de los Avengers a mayúsculas? (Escribe "SI"): ')
        eleccion_mayusculas = eleccion_mayusculas.upper()
        if eleccion_mayusculas == "SI":
            for i in range(len(vengadores)):
                vengadores[i] = vengadores[i].upper()
        else:
            pass

    elif eleccion == "3":
        print("\nSaliendo del programa.")
        break

    elif eleccion == "sacrificar":
        print("SACRIFICANDO A UN AVENGER!!!!!")
        vengadores.pop()

    else:
        print("\nOpción inválida")
