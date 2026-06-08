# Ejercicio 12 — Control de asistencia en una empresa
# Un jefe de RRHH quiere registrar la asistencia de empleados. Ingresa cuántos empleados tiene (entero positivo). Para cada empleado:

# Ingresa su ID (mínimo 6 caracteres, sin espacios)
# Ingresa los días trabajados en el mes (entero de 0 a 23, validado)
# ¿Por qué 0 a 23? Un empleado con licencia médica completa puede tener 0 días trabajados. Algunos meses tienen hasta 23 días hábiles. El rango 0–23 cubre todos los casos reales.

# Clasifica:

# 20 o más días → Asistencia completa
# Menos de 20 días → Asistencia parcial
# Muestra el resumen final.
asistencia = {
    "asistencia_completa": 0,
    "asistencia_parcial": 0,
}
id_totales = []
dias_por_empleado = {}

while True:
    entrada = input("Cuantos empleados tiene \n")
    if not entrada.lstrip("-").isdigit():
        print("Debe ingresar un numero entero")
        continue
    empleados_totales = int(entrada)
    if empleados_totales <= 0:
        print("Debe ser un numero mayor a 0")
        continue
    break

for empleado in range(empleados_totales):
    while True:
        id_empleado = input("Ingrese su ID \n").upper()
        if len(id_empleado) < 6 or " " in id_empleado:
            print("Debe tener 6 o mas caracteres y sin espacios")
            continue
        if id_empleado in id_totales:
            print("ID ya registrado, ingrese otro")
            continue
        break

    print(f"Empleado id : {id_empleado}")
    id_totales.append(id_empleado)

    while True:
        entrada_dias = input("Ingrese cuantos dias ha trabajado \n")
        if not entrada_dias.lstrip("-").isdigit():
            print("Debe ingresar un numero entero")
            continue
        dias_trabajados = int(entrada_dias)
        if dias_trabajados < 0 or dias_trabajados > 23:
            print("Dias invalidos , solamente de 0 a 23")
            continue
        break

    dias_por_empleado[id_empleado] = dias_trabajados

    if dias_trabajados >= 20:
        print("Asistencia completa")
        asistencia["asistencia_completa"] += 1
    else:
        print("Asistencia parcial")
        asistencia["asistencia_parcial"] += 1

print(f"Resumen asistencia : {asistencia}")
print(f"Empleados registrados : {len(id_totales)} de {empleados_totales}")
print(f"IDs registrados : {id_totales}")
print(f"Dias por empleado : {dias_por_empleado}")