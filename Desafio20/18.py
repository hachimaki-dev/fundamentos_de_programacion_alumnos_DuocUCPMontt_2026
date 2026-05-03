numeros = [1, 2, 3, 4]
clasificación = {"pares":[],"impares":[]}
for numero in numeros:
    if numero % 2== 0:
        clasificación["pares"].append(numero)   #Dentro de la llave "pares" usamos .append y luego la variable que va iterando.
    else:
        clasificación["impares"].append(numero)
print(clasificación)