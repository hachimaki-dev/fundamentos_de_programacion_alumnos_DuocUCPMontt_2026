# Ejercicio 13: La Búsqueda (Lista + Condicional)
# Tienes una lista llamada edades.
# Debes contar cuántos valores son mayores o iguales a 18.
# Guarda el resultado en la variable mayores_edad.
# Ejemplo:
# Si edades = [15, 18, 22, 12, 40], entonces mayores_edad = 3.

edades = [15, 18, 22, 12, 40]
mayores_edad = 0

for edad in edades:
    if edad >= 18:
        mayores_edad += 1

print(mayores_edad)
