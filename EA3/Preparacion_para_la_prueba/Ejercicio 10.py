# Ejercicio 10 — Registro de notas de un curso universitario
# El docente ingresa cuántos estudiantes tiene en su curso (entero positivo). Luego, para cada estudiante, ingresa su nota (entero de 1 a 7, validado).

# Al final muestra:

# Cuántos aprobaron (nota ≥ 4)
# Cuántos reprobaron (nota < 4)
# El promedio del curso
# Estructura que debes aplicar:

# 1. Validar N (cantidad de estudiantes)
# 2. for i in range(N):
#        validar nota
#        clasificar y contar
# 3. Mostrar resumen

cantidad_de_estudiantes_aprobados = 0
cantidad_de_estudiantes_reprobados = 0
total_notas = 0


while True:
    try:
        cantidad_de_estudiantes = int(input("Ingrese al cantidad de estudiantes para calificar: "))

        if cantidad_de_estudiantes > 0:
            break

        print("Ingrese un número entero positivo")

    except ValueError:
        print("Ingrese un número entero positivo")


for numero_del_estudiante in range(1, cantidad_de_estudiantes + 1):
    while True:
        try:
            nota_ingresada = float(input(f"Ingrese la nota del estudiante N°{numero_del_estudiante}: "))

            if nota_ingresada > 0.9 and nota_ingresada <= 7:
                break
        
            print("La nota debe estar entre el 1 al 7")

        except ValueError:
            print("Ingrese un número positivo")

    if nota_ingresada >= 4.0:
        print("Aprobado")
        cantidad_de_estudiantes_aprobados += 1
    elif nota_ingresada < 4.0:
        print("Reprobado")
        cantidad_de_estudiantes_reprobados += 1

    total_notas += nota_ingresada
promedio_de_los_estudiantes = total_notas / cantidad_de_estudiantes

print(f"Estudiantes Aprobados: {cantidad_de_estudiantes_aprobados}")
print(f"Estudiantes Reprobados: {cantidad_de_estudiantes_reprobados}")
print(f"El promedio de los estudiantes es de: {float(promedio_de_los_estudiantes)}")