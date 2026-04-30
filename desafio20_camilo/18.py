numeros = [1, 2, 3, 4]

clasificacion = {"Pares" : [], "Impares" : []}

for numero in numeros :
    if numero % 2 == 0 :
        clasificacion["Pares"].append(numero)
    else :
        clasificacion["Impares"].append(numero)

print(clasificacion)