# Ejercicio 12 — Control de asistencia en una empresa

asistencia_completa = 0
asistencia_parcial = 0

while True:

    try:
        cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))

        if cantidad_empleados > 0:
            break

        print("Error: debe ingresar un número positivo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_empleados):

    while True:

        id_empleado = input(f"Ingrese el ID del empleado {i + 1}: ")

        if len(id_empleado) >= 6 and " " not in id_empleado:
            break

        print("ID inválido.")

    while True:

        try:
            dias = int(input("Ingrese los días trabajados: "))

            if 0 <= dias <= 23:
                break

            print("Error: los días deben estar entre 0 y 23.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    if dias >= 20:
        asistencia_completa += 1
    else:
        asistencia_parcial += 1

print()
print(f"Asistencia completa: {asistencia_completa}")
print(f"Asistencia parcial: {asistencia_parcial}")