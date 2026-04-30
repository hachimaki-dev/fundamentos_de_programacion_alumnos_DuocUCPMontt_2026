numeros = range(10)
clasificacion = { "Pares": [], "Impares": [] }

for i in numeros:
    if i % 2 == 0:
        clasificacion["Pares"].append(i)
    else:
        clasificacion["Impares"].append(i)

print(clasificacion)
