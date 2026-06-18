# Ejercicio 22 — Sistema completo de gestión de una clínica veterinaria Parte B

horas_disponibles = 30
capacidad = 30
reservas_activas = 0

historial = []

while True:

    print("\n=== AGENDA CLÍNICA VETERINARIA PATITAS ===")
    print("1. Ver horas disponibles")
    print("2. Reservar hora(s)")
    print("3. Cancelar hora(s)")
    print("4. Ver historial de reservas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        print(f"Horas disponibles: {horas_disponibles}")

    elif opcion == "2":

        try:

            cantidad = int(input("¿Cuántas horas desea reservar?: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número positivo.")

            elif cantidad > horas_disponibles:
                print("Error: no hay suficientes horas disponibles.")

            else:

                horas_disponibles -= cantidad
                reservas_activas += cantidad

                movimiento = {
                    "tipo": "Reserva",
                    "cantidad": cantidad
                }

                historial.append(movimiento)

                print("Reserva realizada correctamente.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "3":

        try:

            cantidad = int(input("¿Cuántas horas desea cancelar?: "))

            if cantidad <= 0:
                print("Error: debe ingresar un número positivo.")

            elif cantidad > reservas_activas:
                print("Error: no puede cancelar más horas de las reservadas.")

            else:

                horas_disponibles += cantidad
                reservas_activas -= cantidad

                movimiento = {
                    "tipo": "Cancelación",
                    "cantidad": cantidad
                }

                historial.append(movimiento)

                print("Cancelación registrada correctamente.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    elif opcion == "4":

        print(f"Reservas activas actualmente: {reservas_activas}")

        print("\nHistorial de movimientos:")

        for movimiento in historial:
            print(movimiento)

    elif opcion == "5":

        print("Gracias por utilizar el sistema. Hasta pronto.")
        break

    else:
        print("Opción inválida.")