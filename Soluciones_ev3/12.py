while True:
    try:
        empleados = int(input("Ingresa la cantidad de empleados: "))
        if empleados > 0:
            break
        else:
            print("ERROR, debe ser entero positivo")
    except ValueError:
        print("ERROR, debe ser entero positivo")

asist_completa = 0
asis_parcial = 0

for i in range(empleados):
    print(f"Empleado {i + 1}")

    while True:
        ID_empleado = input("ID empleado: ")
        if len(ID_empleado) >= 6 and " " not in ID_empleado:
            break
        else:
            print("El ID debe contener min 6 caracteres y no espacios")
        
    while True:
        try:
            dias = int(input("Ingresa la cantidad de dias trabajados: "))
            if dias >= 0 and dias <= 23:
                break
            else:
                print("ERROR, los dias debe ser de 0 a 23")
        except ValueError:
            print("ERROR, debe ser un numero entero")
        
        if dias >= 20:
            print("Asistencia completa")
            asist_completa += 1
        else:
            print("Asistencia parcial")
            asis_parcial += 1

print(f"Asistencias completas: {asist_completa}")
print(f"Asistencias Parciales: {asis_parcial}")
