# Tienes una lista llamada edades.

# Debes contar cuántos valores son mayores o iguales a 18.

# Guarda el resultado en la variable mayores_edad.

edades = [12,45,89,18,9,21]

mayores_edad = 0

for edad in edades:
    if edad >= 18:
        mayores_edad += 1

print(mayores_edad)