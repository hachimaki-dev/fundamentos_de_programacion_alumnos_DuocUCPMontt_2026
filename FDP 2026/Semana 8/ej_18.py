# Tienes una lista llamada numeros.

# Debes clasificar sus valores en un diccionario llamado clasificacion:

#    en la lista clasificacion['pares'] debes guardar los números pares
#    en la lista clasificacion['impares'] debes guardar los números impares

numeros = [1,41,62,37,8,90,77,67,21]

clasificacion = {"pares": 0, "impares": 0}

for numero in numeros:
    if numero % 2 == 0:
        clasificacion.update({"pares": clasificacion.get("pares") + 1})
    else:
        clasificacion.update({"impares": clasificacion.get("impares") + 1})

print(clasificacion)