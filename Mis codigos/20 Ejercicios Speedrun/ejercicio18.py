# Define la lista numeros = [1, 2, 3, 4]. Crea un diccionario llamado clasificacion con esta estructura:
# {'pares': [], 'impares': []}
# Recorre la lista y guarda cada número en la lista correspondiente según si es par o impar. Imprime el diccionario final.

numeros = [1, 2, 3, 4]
clasificacion = {"pares": [], "impares": []}

for numero in numeros:
    if numero % 2 == 0:
        clasificacion["pares"].append(numero)
    else:
        clasificacion["impares"].append(numero)

print(clasificacion)