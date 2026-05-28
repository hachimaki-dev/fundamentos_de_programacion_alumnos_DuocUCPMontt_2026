def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

datos = [10, 20, 30]
resultado = sumar_lista(datos)
print(resultado * 2)