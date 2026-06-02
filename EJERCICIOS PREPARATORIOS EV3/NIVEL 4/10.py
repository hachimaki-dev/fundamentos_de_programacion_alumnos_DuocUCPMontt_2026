#Ejercicio 10 — Registro de notas de un curso universitario
#El docente ingresa cuántos estudiantes tiene en su curso (entero positivo). Luego, para cada estudiante, ingresa su nota (entero de 1 a 7, validado).

#Al final muestra:

#Cuántos aprobaron (nota ≥ 4)
#Cuántos reprobaron (nota < 4)
#El promedio del curso
#Estructura que debes aplicar:

#1. Validar N (cantidad de estudiantes)
#2. for i in range(N):
       #validar nota
       #clasificar y contar
#3. Mostrar resumen

while True:
    try:
        n = int(input("Ingresa la cantidad de estudiantes (en formato numérico): "))
        if n > 0:
            break
        else:
            print("Error: la cantidad de estudiantes debe ser mayor que 0")
    except ValueError:
        print("Error: ingrese un número entero positivo válido")

aprobado = 0
reprobado = 0
suma_notas = 0

for i in range(n):
    while True:
        try:
            nota_estudiante = int(input(f"Ingrese la calificación del estudiante {i + 1}: "))
            if nota_estudiante < 1:
                print("Error: la calificación no puede ser un número menor que 1")
            elif nota_estudiante > 7:
                print("Error: la califiación no puede ser mayor que 7")
            else:
                break
        except ValueError:
            print("Ingrese una calificación válida, debe ser un número entero positivo")
    
    suma_notas += nota_estudiante

    if nota_estudiante >= 4:
        aprobado += 1
        print("Aprobado")
    else:
        reprobado += 1
        print("Reprobado")
    
promedio_curso = suma_notas / n

print("\n----------------------------------------------")
print(f"Estudiantes aprobados = {aprobado}")
print(f"Estudiantes reprobados = {reprobado}")
print(f"Promedio del curso = {promedio_curso:.1f}")
print("------------------------------------------------")