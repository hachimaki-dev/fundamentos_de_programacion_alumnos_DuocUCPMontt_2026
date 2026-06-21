def promedio(lista):
    if len(lista) == 0:
        return 0
    suma_total = 0
    for numero in lista:
        suma_total += numero
    return suma_total / len(lista)
notas = [6, 7, 7]
resultado = promedio(lista=notas)
print(resultado)