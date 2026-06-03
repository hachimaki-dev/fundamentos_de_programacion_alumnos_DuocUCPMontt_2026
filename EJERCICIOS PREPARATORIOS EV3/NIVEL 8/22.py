#PARTE A
grandes = 0
pequeños = 0

while True:
    try:
        pacientes = int(input("Catidad de pacientes: "))
        if pacientes <= 0:
            print("Error: La cantidad de pacientes debe ser mayor a 0.")
        else:
            break
    except ValueError:
        print("Error: Ingresa una cantidad válida.")

for p in range(pacientes):

    while True:
        ID_animal = input(f"ID animal {p + 1}: ").strip().upper()
        if len(ID_animal) >= 6 and " " not in ID_animal:
            break
        else:
            print("Error: El ID del animal debe tener mínimo 6 caracteres, sin espacios.")
    
    while True:
        try:
            peso = int(input(f"Peso en Kg del animal {ID_animal}: "))
            if peso <= 0:
                print("Error: El peso registrado debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error: EL peso debe ingresarse en formato numérico.")

    if peso > 25:
        grandes += 1
    else:
        pequeños += 1

print(f"La clínica ha registrado {grandes} pacientes grandes y {pequeños} pacientes pequeños. ¡Bienvenidos!")

# PARTE B
horas_disponibles = 30
historial = 0

menu = ["1", "2", "3", "4", "5"]

while True:
    print("""=== AGENDA CLÍNICA VETERINARIA PATITAS ===
1. Ver horas disponibles
2. Reservar hora(s)
3. Cancelar hora(s)
4. Ver historial de reservas
5. Salir""")

    while True:
        opcion = input(":")
        if opcion in menu:
            break
        else:
            print("Error: Ingresa una opción válida.")
    
    if opcion == "5":
        print(f"Hay {horas_disponibles} horas disponibles. Se cerró la agenda.")
        break

    elif opcion == "1":
        print(f"Hay {horas_disponibles} horas disponibles.")

    elif opcion == "2":
        while True:
            try:
                reservar = int(input("Registre la hora(S) a reservar: "))
                if reservar <= 0:
                    print("Error: Las horas deben ser mayores a 0.")
                elif reservar > horas_disponibles:
                    print("Error: No puedes reservar más horas de las disponibles.")
                else:
                    horas_disponibles -= reservar
                    historial += reservar
                    if horas_disponibles == 0:
                        print("No hay horas disponibles.")
                    else:
                        print(f"Reservaste {reservar} hora(S).")
                        print(f"Actualmente, hay {horas_disponibles} horas disponibles.")
                    break
            except ValueError:
                print("Error: Ingrese una hora válida.")
    
    elif opcion == "3":
        while True:
            try:
                cancelar = int(input("Hora(s) a cancelar: "))
                if cancelar <= 0:
                    print("Error: las horas deben ser mayores a 0.")
                elif cancelar > historial:
                    print("Error: No se pueden cancelar más horas que las registradas.")
                else:
                    horas_disponibles += cancelar
                    historial -= cancelar
                    print(f"Cancelaste {cancelar} hora(S).")
                    print(f"Actualmente, hay {horas_disponibles} horas disponibles.")
                    break
            except ValueError:
                print("Error: Ingrese una hora válida.")
    
    else:
        print(f"Se han ocupado {historial} hora(s).")