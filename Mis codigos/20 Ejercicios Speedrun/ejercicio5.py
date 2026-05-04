# Ejercicio 5: Ciclo For y Rango
# Usa un ciclo for con range() para sumar todos los números del 0 al 10, incluyendo el 10.
# Guarda el resultado en la variable resultado.
# Pista: recuerda que range(11) llega hasta 10.

resultado = 0

for numero in range(11):
    resultado += numero

print(resultado)