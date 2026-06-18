# Ejercicio 21 — Sistema de gestión de mesas en un restaurante

mesas_disponibles = 20
capacidad = 20
mesas_ocupadas = 0

movimientos = []

while True:

    print("\n=== SISTEMA DE MESAS - RESTAURANTE EL FARO ===")
    print("1. Ver mesas disponibles")
    print("2. Asignar mesa(s)")
    print("3. Liberar mesa(s)")
    print("4. Mesas ocupadas actualmente")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        print(f"Mesas disponibles: {mesas_disponibles}")

    elif opcion == "2":

        try:

            cantidad = int(input("Cantidad de mesas a asignar: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número positivo.")

            elif cantidad > mesas_disponibles:
                print("Error: no hay suficientes mesas disponibles.")

            else:

                mesas_disponibles -= cantidad
                mesas_ocupadas += cantidad

                movimiento = {
                    "tipo": "Asignación",
                    "cantidad": cantidad
                }

                movimientos.append(movimiento)

                print("Mesas asignadas correctamente.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "3":

        try:

            cantidad = int(input("Cantidad de mesas a liberar: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número positivo.")

            elif cantidad > mesas_ocupadas:
                print("Error: no hay tantas mesas ocupadas.")

            else:

                mesas_disponibles += cantidad
                mesas_ocupadas -= cantidad

                movimiento = {
                    "tipo": "Liberación",
                    "cantidad": cantidad
                }

                movimientos.append(movimiento)

                print("Mesas liberadas correctamente.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "4":

        print(f"Mesas ocupadas actualmente: {mesas_ocupadas}")

        print("\nHistorial:")

        for movimiento in movimientos:
            print(movimiento)

    elif opcion == "5":

        print("Servicio finalizado. Buenas noches.")
        break

    else:
        print("Opción inválida.")