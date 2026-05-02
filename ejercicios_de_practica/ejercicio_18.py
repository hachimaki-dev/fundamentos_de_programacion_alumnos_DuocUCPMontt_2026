numeros = [10, 40, 23, 15, 65, 2]

clasificacion = {"pares": [], "impares": []}

for numero in numeros:
    if numero % 2 == 0:
        clasificacion["pares"].append(numero)

    else:
        clasificacion["impares"].append(numero)

print(f"Pares: {clasificacion["pares"]}")
print(f"Impares: {clasificacion["impares"]}")