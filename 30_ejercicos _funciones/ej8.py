def crear_pares(lista_numeros):
    lista_pares = []
    for numeros in lista_numeros:
        if numeros % 2 == 0:
            lista_pares.append(numeros)
    return lista_pares
resultado = crear_pares(lista_numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(resultado)