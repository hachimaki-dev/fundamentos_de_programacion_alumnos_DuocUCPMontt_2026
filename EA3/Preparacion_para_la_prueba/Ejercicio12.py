# Ejercicio 12 — Control de asistencia en una empresa
# Un jefe de RRHH quiere registrar la asistencia de empleados. Ingresa cuántos empleados tiene (entero positivo). Para cada empleado:

# Ingresa su ID (mínimo 6 caracteres, sin espacios)
# Ingresa los días trabajados en el mes (entero de 0 a 23, validado)
# ¿Por qué 0 a 23? Un empleado con licencia médica completa puede tener 0 días trabajados. Algunos meses tienen hasta 23 días hábiles. El rango 0–23 cubre todos los casos reales.

# Clasifica:

# 20 o más días → Asistencia completa
# Menos de 20 días → Asistencia parcial
# Muestra el resumen final.

while True:
    try:
        cantidad_de_empleados_de_la_empresa = int(input("Ingrese la cantidad de empleados: "))

        if cantidad_de_empleados_de_la_empresa < 1:
            print("Ingrese un número de entero positivo")
        else:
            break
    except ValueError:
        print("ValueError: Ingrese un número entero positivo")

asistencia_completa = 0
asistencia_parcial = 0
asistencia_total = 0

for i in range(1, cantidad_de_empleados_de_la_empresa + 1):
    while True:
        try:
            id_del_empleado = input(f"Ingrese ID del empleado N°{i}: ")

            if len(id_del_empleado) >= 6 and " " not in id_del_empleado:
                print(f"Ingresado el ID del empleado N°{i} es: {id_del_empleado}")
                break
            else:
                print("Ingrese mínimo 6 caracteres, sin espacios validos")

        except ValueError:
            print("Ingrese un caracter valido")
    while True:
        try:
            dias_trabajados = int(input(f"Ingrese los días trabajados del empleado {i} con el id {id_del_empleado}: "))
            
            if dias_trabajados > -1 and dias_trabajados <= 23:
                print("Ingreso exitoso")
                break
            else:
                print("Ingrese los días trabajados entre el 1 al 23 (entero positivos)")
        except ValueError:
            print("Ingrese números enteros positivos")
    
    if dias_trabajados >= 20:
        asistencia_completa += 1
    else:
        asistencia_parcial += 1
    
    asistencia_total = asistencia_completa + asistencia_parcial

print(f"Asistencia Completa: {asistencia_completa}")
print(f"Asistencia Parcial: {asistencia_parcial}")
print(f"Asistencia Total: {asistencia_total}")