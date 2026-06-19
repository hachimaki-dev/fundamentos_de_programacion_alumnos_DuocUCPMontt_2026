while True:
    try:
        n = int(input("¿Cuántos empleados tiene? "))
        if n > 0:
            break
        print("Error: debe ser un entero positivo.")
    except ValueError:
        print("Error: debe ser un entero positivo.")

completa = 0
parcial  = 0

for i in range(n):
    print("\n--- Empleado", i+1, "---")

    # validar ID
    while True:
        id_emp = input("  ID del empleado: ").strip()
        if len(id_emp) >= 6 and " " not in id_emp:
            break
        print("  Error: mínimo 6 caracteres, sin espacios.")

    while True:
        try:
            dias = int(input("  Días trabajados este mes (0-23): "))
            if dias >= 0 and dias <= 23:
                break
            print("Error: debe estar entre 0 y 23.")
        except ValueError:
            print("Error: ingresa un número entero.")

    if dias >= 20:
        print("Asistencia completa")
        completa += 1
    else:
        print("Asistencia parcial")
        parcial += 1

print('Resumen')
print('Asistencia completa:", completa, "empleados')
print('Asistencia parcial: ", parcial, "empleados')