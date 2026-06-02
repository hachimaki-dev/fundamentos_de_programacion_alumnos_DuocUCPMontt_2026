#Ejercicio 12 — Control de asistencia en una empresa
#Un jefe de RRHH quiere registrar la asistencia de empleados. Ingresa cuántos empleados tiene (entero positivo). Para cada empleado:

#Ingresa su ID (mínimo 6 caracteres, sin espacios)
#Ingresa los días trabajados en el mes (entero de 0 a 23, validado)
#¿Por qué 0 a 23? Un empleado con licencia médica completa puede tener 0 días trabajados. Algunos meses tienen hasta 23 días hábiles. El rango 0–23 cubre todos los casos reales.

#Clasifica:

#20 o más días → Asistencia completa
#Menos de 20 días → Asistencia parcial
#Muestra el resumen final.

while True:
    try:
        empleados = int(input("Ingresa la cantidad de empleados: "))
        if empleados > 0:
            break
        else:
            print("Error: La cantidad de empleados no puede ser menor o igual a 0.")
    except ValueError:
        print("Ingresa un número entero positivo válido.")

asistencia_completa = 0
asistencia_parcial = 0

for i in range(empleados):
    while True:
        id_empleado = input(f"Ingrese ID del empleado {i + 1}: ").strip()
        if len(id_empleado) >= 6 and " " not in id_empleado:
            break
        else:
            print("Error: la ID del empleado debe tener mínimo 6 caracteres, sin espacios")
    
    while True:
        try:
            dias_trabajados = int(input(f"Ingresa los días trabajados del empleado {id_empleado}: "))
            if dias_trabajados < 0:
                print("Error: Los días trabajados no pueden ser menor a 0")
            elif dias_trabajados > 23:
                print("Error: Los días trabajados no puede ser mayor a 23 días hábiles")
            else:
                break
        except ValueError:
            print("Error: Ingrese los días trabajados en formato númerico, solo enteros")

    if dias_trabajados >= 20:
        asistencia_completa += 1
        print("Asistencia completa")
    else:
        asistencia_parcial += 1
        print("Asistencia parcial")

print("\n-----------------RESUMEN------------------------")
print(f"Asistencia completa = {asistencia_completa} empleados")
print(f"Asistencia parcial = {asistencia_parcial} empleados")
print("---------------------------------------------------")