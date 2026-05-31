flag = True
while flag:
    try:
        cantidad_de_estudiantes = int(input("Profesor, ¿cuantos alumnos tiene su curso? "))
        if cantidad_de_estudiantes <= 0:
            print("Ingrese un número entero positivo de estudiantes.")
        else:
            print(f"La cantidad de estudiantes es de {cantidad_de_estudiantes}.")
            flag = False
    except ValueError:
        print("Ingrese números, no letras, puntos u otros caracteres especiales.")
promedio = 0
aprobados = 0
reprobados = 0
for alumno in range(1,cantidad_de_estudiantes+1):
    while True:
        try:
            nota_por_estudiante = float(input(f"Ingrese nota del alumno n°{alumno}: "))
            if nota_por_estudiante >= 1 and nota_por_estudiante <= 7:
                break
            else:
                print("La nota debe estar dentro de un rango de 1 y 7.")
        except ValueError:
            print("Ingrese notas válidas.")
        
    if nota_por_estudiante >= 4:
        promedio += nota_por_estudiante
        aprobados +=1
    else: 
        promedio+= nota_por_estudiante
        reprobados +=1

print(f"Alumnos aprobados: {aprobados}.")
print(f"Alumnos reprobados: {reprobados}.")
print(f"El promedio de las notas fue de {round(promedio/cantidad_de_estudiantes, 2)}.")