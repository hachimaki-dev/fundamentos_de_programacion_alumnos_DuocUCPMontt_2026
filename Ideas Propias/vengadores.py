# 🔴 Reto Avanzado: Ensamblando a los Vengadores

vengadores = []

while True:

    print("===== BASE DE LOS AVENGERS =====")
    print("1 - Agregar Avenger")
    print("2 - Mostrar Base y Modificar")
    print("3 - Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del héroe: ")
        vengadores.append(nombre)
        print("Avenger agregado a la base.")

    elif opcion == "2":

        if len(vengadores) == 0:
            print("La base está vacía.")
        else:

            print("=== Lista de Avengers ===")

            for i in range(len(vengadores)):
                print(f"{i} - vengadores{[i]}")

                vengadores[i] = vengadores[i].upper()

            print("Base actualizada a MAYÚSCULAS.")

            palabra = input("¿Palabra secreta? ")

            if palabra == "Sacrificar":
                if len(vengadores) > 0:
                    eliminado = vengadores.pop()
                    print(f"{eliminado} fue enviado contra Thanos.")

    elif opcion == "3":
        print("Nick Fury cerró la base.")
        break

    else:
        print("Opción inválida.")