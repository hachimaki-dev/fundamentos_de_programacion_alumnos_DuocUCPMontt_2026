# Ejercicio 5: Ciclo For y Rango
# Usa un ciclo for con range() para sumar todos los números del 0 al 10, incluyendo el 10.
# Guarda el resultado en la variable resultado.
# Pista: recuerda que range(11) llega hasta 10.

resultado = 0

for i in range(0,11):
    print(i)
    resultado += i
print(f"La suma total es: {resultado}")    