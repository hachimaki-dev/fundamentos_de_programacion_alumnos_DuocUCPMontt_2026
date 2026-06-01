while True:
    try:
        numero_estudiantes = int(input("Ingrese la cantidad de estudiantes de su curso: "))
        if numero_estudiantes <= 0:
            print("Dato inválido. Debe haber al menos 1 estudiante.")
        else:
            break
    except ValueError:
        print("Dato inválido. Ingresa un número entero positivo.")

aprobados = 0
reprobados = 0
suma_notas = 0

for i in range(1, numero_estudiantes + 1):

    while True:
        try:
            nota_estudiante = float(input(f"Ingresa la nota del estudiante {i} (1 a 7): "))
            if nota_estudiante < 1.0 or nota_estudiante > 7.0:
                print("Nota fuera de rango. Debe ser entre 1.0 y 7.0.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Ingresa un número entero (ej: 4.5) o entero")
        
    suma_notas += nota_estudiante

    if nota_estudiante >= 4:
        aprobados += 1
    elif nota_estudiante < 4:
        reprobados += 1
promedio_curso = suma_notas / numero_estudiantes

print("---- Resumen ----")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobados: {reprobados}")
print(f"Promedio del curso: {promedio_curso}")