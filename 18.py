numeros = [1, 2, 3, 4]

clasificacion = {
    'pares': [],
    'impares': []
}

for num in numeros:
    if num % 2 == 0:
        clasificacion['pares'].append(num)
    else:
        clasificacion['impares'].append(num)

print(clasificacion)