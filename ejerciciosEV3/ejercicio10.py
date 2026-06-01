""" Ejercicio 10 — Registro de notas de un curso universitario
El docente ingresa cuántos estudiantes tiene en su curso (entero positivo). Luego, para cada estudiante, ingresa su nota (entero de 1 a 7, validado).

Al final muestra:

Cuántos aprobaron (nota ≥ 4)
Cuántos reprobaron (nota < 4)
El promedio del curso


Estructura que debes aplicar:
1. Validar N (cantidad de estudiantes)
2. for i in range(N):
       validar nota
       clasificar y contar
3. Mostrar resumen """





notas = []
aprovados = 0
reprobados = 0
promedio_curso = 0

while True:
    try:
        estudiantes = int(input("ingresa la cantidad de estudiantes : "))
        if estudiantes > 0:
            break
        else:
            print("ingresa un numero valido de estudiantes")
    except:
        print("ingresa un numero real")


for cantidad_de_notas in range(estudiantes):
    while True:
        try:
            nota = int(input(f"ingresa la nota del estudiante {cantidad_de_notas + 1} (tiene que ser del 1 al 7)"))
            promedio_curso +=nota / estudiantes
            if nota >=1 and nota <=7:
                break
            else:
                print("la nota tiene que ser en el rango de numero entero del 1 al 7")
        except ValueError:
            print("ingrese la nota como numero valido")
    
    
    notas.append(nota)
    if nota >= 4:
        aprovados+=1
    elif nota < 4:
        reprobados +=1

print(f"resumen :\n cantidad de aprobados : {aprovados}\n cantidad de reprobados : {reprobados}\n promedio curso : {promedio_curso} ")







