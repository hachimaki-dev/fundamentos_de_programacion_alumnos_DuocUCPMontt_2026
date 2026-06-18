# Ejercicio 16 — Gestión de turnos en un servicio de urgencias

pacientes = 0
capacidad = 25
historial = 0

while True:

    print("=== URGENCIAS HOSPITAL REGIONAL ===")
    print("1. Ver pacientes en sala")
    print("2. Registrar ingreso de paciente(s)")
    print("3. Registrar alta de paciente(s)")
    print("4. Total de ingresos del turno")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Pacientes en sala: {pacientes}")

    elif opcion == "2":

        try:
            ingreso = int(input("Cantidad de pacientes que ingresan: "))

            if ingreso <= 0:
                print("Debe ingresar un valor positivo.")

            elif pacientes + ingreso > capacidad:
                print("Capacidad máxima excedida.")

            else:
                pacientes += ingreso
                historial += ingreso

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "3":

        try:
            alta = int(input("Cantidad de altas: "))

            if alta <= 0:
                print("Debe ingresar un valor positivo.")

            elif alta > pacientes:
                print("No hay tantos pacientes en sala.")

            else:
                pacientes -= alta
                historial -= alta

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "4":
        print(f"Total de ingresos del turno: {historial}")

    elif opcion == "5":
        print("Sesión finalizada.")
        break

    else:
        print("Opción inválida.")