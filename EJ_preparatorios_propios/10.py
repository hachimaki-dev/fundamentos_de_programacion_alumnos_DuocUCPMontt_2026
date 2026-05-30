aprobados = 0
reprobados = 0
sumar_notas = 0

while True:
    try:
        cantidad_de_estudiantes = int(input("Cuantos estudiantes  tiene su curso :  "))
        break
    except ValueError:
        print("Ingrese una opcion valida")
        continue


for i in range(cantidad_de_estudiantes):
    try:
        nota_cada_estudiante = int(input("Ingrese su nota :  "))
        sumar_notas += nota_cada_estudiante     
    except ValueError:
        print("Ingrese una opcion valida")
        continue
    if nota_cada_estudiante >= 4:
        aprobados += 1
    else:
        reprobados += 1


promedio_notas_estudiantes = sumar_notas / cantidad_de_estudiantes

print()
print(f"Aprobados : {aprobados}")
print(f"Reprobados : {reprobados}")
print(f"Promedio del curso : {promedio_notas_estudiantes}")

