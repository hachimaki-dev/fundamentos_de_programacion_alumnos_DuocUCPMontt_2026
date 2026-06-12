while True:
    try:
        n = int(input("Cantidad de estudiantes: "))
        break
    except ValueError:
        print("Debe ingresar un número entero.")

aprobados = 0
reprobados = 0
suma_notas = 0

for i in range(n):
    while True:
        try:
            nota = int(input("Ingrese nota: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    suma_notas += nota

    if nota >= 4:
        aprobados += 1
    else:
        reprobados += 1

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio:", suma_notas / n)