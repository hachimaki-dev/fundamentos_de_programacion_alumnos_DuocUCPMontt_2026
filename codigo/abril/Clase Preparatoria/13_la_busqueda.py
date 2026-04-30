edades = [ 15, 18, 22, 12, 40 ]
mayores_edad = 0

for i in edades:
    if i >= 18:
        mayores_edad = mayores_edad + 1
    else:
        continue

print(mayores_edad)
