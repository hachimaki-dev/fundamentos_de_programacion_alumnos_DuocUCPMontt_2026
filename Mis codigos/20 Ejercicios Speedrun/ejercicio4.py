# Ejercicio 4: Ciclo While Básico
# Usa un ciclo while para sumar los números del 1 al 5.
# Debes guardar el resultado final en la variable suma.
# Pista: puedes usar una variable contador que comience en 1 y vaya aumentando.

suma = 0
contador = 1

while contador < 6:
    suma += contador
    contador += 1

print(suma)