
while True:
    try:
        estudiantes = int(input('¿Cuantos estudiante tiene el curso?: '))
        if estudiantes > 0:
            break
        else:
            print('Error debe ser un numero positivo y entero')
    except ValueError:
         print('Error debe ser un numero positivo entero''')

aprobados = 0
reprobados = 0
notas_totales = 0

for i in range(7):

    while True:
        try:
            nota = int(input(f'Nota de los estudiante (1 a 7) {i + 1}: '))
            if nota >= 1 and nota <= 7:
                break
            else:
                print('Error la nota debe ser de 1 a 7')
        except ValueError:
            print('Error ingrese un numero entero positivo')  

    notas_totales += nota        

    if nota >= 4:  
        aprobados += 1
    else:
        reprobados -= 1

promedio = notas_totales / nota

print('--------------')
print('Resumen')
print('Aprobados: ', aprobados)
print('Reporbados: ', reprobados)
print('Promedio: ', promedio)