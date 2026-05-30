while True:
    try:
        estudiantes = int(input("Ingrese la cantidad de estudiantes en el curso: "))
        if estudiantes > 0:
            break
        else:
            print("ERROR, debe ser un entero positivo")
    except ValueError:
        print("ERROR, solo enteros positivos")

aprobados = 0
reprobados = 0
total_notas = 0
for i in range(estudiantes):
    while True:
        try:
            nota = int(input(f"Ingrese la nota del estudiante {i + 1} (1 al 7): "))
            if nota >= 1 and nota <= 7:
                break
            else:
                print("ERROR, la nota debe de ser de 1 a 7")
        except ValueError:
            print("ERROR, ingrese un numero entero")
    
    total_notas += nota
    if nota >= 4:
        print("Aprobado")
        aprobados +=1
    else:
        print("Reprobado")
        reprobados += 1

promedio_curso = total_notas / estudiantes
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Promedio: {promedio_curso}")







