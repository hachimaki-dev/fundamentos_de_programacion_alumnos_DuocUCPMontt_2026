# Ejercicio 10 — Registro de notas de un curso universitario

aprobados = 0
reprobados = 0
suma_notas = 0

while True:

    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

        if cantidad_estudiantes > 0:
            break

        print("Error: debe ingresar un número positivo.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_estudiantes):

    while True:

        try:
            nota = int(input(f"Ingrese la nota del estudiante {i + 1}: "))

            if 1 <= nota <= 7:
                break

            print("Error: la nota debe estar entre 1 y 7.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    suma_notas += nota

    if nota >= 4:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma_notas / cantidad_estudiantes

print()
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Promedio del curso: {promedio}")