edades = [15, 16, 20, 40, 12, 18, 3, 10]

mayores_edad = 0

for edad in edades:
    if edad >= 18:
        mayores_edad += 1

print(f"De la lista hay {mayores_edad} personas mayores de edad")