# Ejercicio 4: Ciclo While Básico
# Usa un ciclo while para sumar los números del 1 al 5.
# Debes guardar el resultado final en la variable suma.
# Pista: puedes usar una variable contador que comience en 1 y vaya aumentando.

contador = 1
suma = 0

while contador <= 5:
    suma = suma + contador
    print(f"Numero: {contador}")
    contador += 1

print(f"El resultado total es: {suma}")