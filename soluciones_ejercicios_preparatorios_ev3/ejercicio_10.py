alumnos_aprobados = 0
alumnos_reprobados = 0
promedio_de_notas_del_curso = 0
acumulador_de_notas = 0
while True:
    try:
        numero_alumnos_del_curso = int(input("Ingrese el número de alumnos evaluados: "))
        if numero_alumnos_del_curso <= 0:
            print("Ingrese un número entero válido")
        else:
            break
    except ValueError:
        print("Ingrese un número entero válido")

for indice_alumno in range(1,(numero_alumnos_del_curso +1)):
    while True:
        try:
            nota_alumno_i = int(input(f"Ingrese la nota del alumno {indice_alumno}: "))
            if nota_alumno_i < 1 or nota_alumno_i > 7:
                print("Ingrese una nota entera del 1 al 7")
            else:
                acumulador_de_notas += nota_alumno_i
                break    
        except ValueError:
            print("Ingrese una nota entera del 1 al 7")
    if nota_alumno_i >= 4:
        alumnos_aprobados += 1
    else:
        alumnos_reprobados += 1
promedio_de_notas_del_curso = acumulador_de_notas // numero_alumnos_del_curso
print(f" Alumnos reprobados: {alumnos_reprobados}\n Alumnos aprobados: {alumnos_aprobados}\n Promedio del curso: {promedio_de_notas_del_curso}")    