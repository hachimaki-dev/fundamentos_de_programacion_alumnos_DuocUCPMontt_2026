# Ejercicio 17 — Control de aforo en un evento masivo

cupos = 500
ingresados = 0

while True:

    print("=== CONTROL DE ACCESO - FESTIVAL AUSTRAL ===")
    print("1. Ver cupos disponibles")
    print("2. Registrar entrada de grupo")
    print("3. Registrar salida de grupo")
    print("4. Total de personas que han ingresado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Cupos disponibles: {cupos}")

    elif opcion == "2":

        try:
            grupo = int(input("Cantidad de personas que ingresan: "))

            if grupo <= 0:
                print("Debe ingresar un valor positivo.")

            elif grupo > cupos:
                print("No hay suficientes cupos disponibles.")

            else:
                cupos -= grupo
                ingresados += grupo

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "3":

        try:
            grupo = int(input("Cantidad de personas que salen: "))

            if grupo <= 0:
                print("Debe ingresar un valor positivo.")

            elif cupos + grupo > 500:
                print("No pueden salir más personas de las que han entrado.")

            else:
                cupos += grupo
                ingresados -= grupo

        except ValueError:
            print("Debe ingresar un número entero.")

    elif opcion == "4":
        print(f"Total de personas actualmente dentro del evento: {ingresados}")

    elif opcion == "5":
        print("Control de acceso finalizado.")
        break

    else:
        print("Opción inválida.")