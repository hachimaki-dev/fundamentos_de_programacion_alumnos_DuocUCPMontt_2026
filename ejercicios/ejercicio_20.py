# Ejercicio 20 — Sistema de préstamos de equipos en una universidad

equipos_disponibles = 60
capacidad_maxima = 60
prestamos_activos = 0

movimientos = []

while True:

    print("\n=== BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR ===")
    print("1. Ver equipos disponibles")
    print("2. Prestar equipo(s)")
    print("3. Recibir devolución")
    print("4. Ver historial de préstamos activos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        print(f"Equipos disponibles: {equipos_disponibles}")

    elif opcion == "2":

        try:

            cantidad = int(input("Cantidad de equipos a prestar: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número positivo.")

            elif cantidad > equipos_disponibles:
                print("Error: no hay suficientes equipos disponibles.")

            else:

                equipos_disponibles -= cantidad
                prestamos_activos += cantidad

                movimiento = {
                    "tipo": "Préstamo",
                    "cantidad": cantidad
                }

                movimientos.append(movimiento)

                print("Préstamo registrado.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "3":

        try:

            cantidad = int(input("Cantidad de equipos devueltos: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número positivo.")

            elif cantidad > prestamos_activos:
                print("Error: no se pueden devolver más equipos de los prestados.")

            else:

                equipos_disponibles += cantidad
                prestamos_activos -= cantidad

                movimiento = {
                    "tipo": "Devolución",
                    "cantidad": cantidad
                }

                movimientos.append(movimiento)

                print("Devolución registrada.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "4":

        print(f"Equipos actualmente prestados: {prestamos_activos}")

        print("\nMovimientos registrados:")

        for movimiento in movimientos:
            print(movimiento)

    elif opcion == "5":

        print("Gracias por utilizar el sistema. Hasta pronto.")
        break

    else:
        print("Opción inválida.")