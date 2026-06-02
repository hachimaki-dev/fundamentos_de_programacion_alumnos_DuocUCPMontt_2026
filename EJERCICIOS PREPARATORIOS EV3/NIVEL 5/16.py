#Ejercicio 16 — Gestión de turnos en un servicio de urgencias
#Un hospital gestiona los turnos de atención en urgencias. Comienza con 0 pacientes en sala. #Capacidad máxima: 25 pacientes.

#=== URGENCIAS HOSPITAL REGIONAL ===
#1. Ver pacientes en sala
#2. Registrar ingreso de paciente(s)
#3. Registrar alta de paciente(s)
#4. Total de ingresos del turno
#5. Salir
#Reglas:

#No puede haber más pacientes que la capacidad máxima
#No se puede dar de alta más pacientes de los que hay
#El historial de ingresos aumenta con cada ingreso y disminuye con cada alta (igual que en la evaluación)

opcion = 0
sala  = 0
historial = 0
capacidad_max = 25

while True:
    print("\n=== URGENCIAS HOSPITAL REGIONAL ===")
    print("1. Ver pacientes en sala")
    print("2. Registrar ingreso de paciente(s)")
    print("3. Registrar alta de paciente(s)")
    print("4. Total de ingresos del turno")
    print("5. Salir")


    while True:
        try:
            opcion = int(input("Ingresa número de la opción: "))
            if 1 <= opcion <= 5:
                break
            else:
                print("Error: Ingrese una opción válida")
        except ValueError:
            print("Error: Ingrese una opción válida")
    
    if opcion == 5:
        print(f"Cantidad de pacientes en sala final: {sala}")
        print("Saliste del programa")
        break

    elif opcion == 1:
        print(f"\nActualmente, hay {sala} pacientes en sala")

    elif opcion == 2:
        while True:
            try:
                ingreso = int(input("\nCantidad de pacientes que ingresan: "))
                if ingreso <= 0:
                    print("Error: Los ingresos deben ser mayores a 0.")
                elif (ingreso + sala) > capacidad_max:
                    print("Error: Capacidad máxima de la sala de urgencias superada.")
                else:
                    historial += ingreso
                    sala += ingreso
                    if sala == capacidad_max:
                        print("Capacidad máxima alcanzada.")
                    print(f"Ingresaste {ingreso} pacientes.")
                    break
            except ValueError:
                print("Error: Ingresa una cantidad válida.")

    elif opcion == 3:
        while True:
            try:
                salida = int(input("\nCantidad de pacientes dados de alta: "))
                if salida <= 0:
                    print("Error: Las altas deben ser mayores a 0.")
                elif salida > sala:
                    print("Error: No se puede dar de alta a más pacientes de los que hay.")
                else:
                    historial -= salida
                    sala -= salida
                    print(f"{salida} pacientes fueron dados de alta.")
                    break
            except ValueError:
                print("Error: Ingresa una cantidad válida.")

    elif opcion == 4:
        print(f"\nTotal de ingresos: {historial} pacientes")