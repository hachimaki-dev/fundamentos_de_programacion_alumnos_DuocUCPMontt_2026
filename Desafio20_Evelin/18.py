numeros = [1, 2, 3, 4]
clasificacion = {'pares': [], 'impares': []}
for numero in numeros:
    if numero % 2 == 0:
        clasificacion['pares'].append(numero)
    else:
        clasificacion['impares'].append(numero)

print(clasificacion)