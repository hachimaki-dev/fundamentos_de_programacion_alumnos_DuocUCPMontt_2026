lista_jiiji = [1, 2, 3, 4]
def crear_pares(lista_numeros):
    lista_pares = []
    for numeros in lista_numeros:
        if numeros % 2 == 0:
            lista_pares.append(numeros)
    return lista_pares
def sumar(a, b):
    return (a + b)
def sumar_pares_lista(lista):
    solo_pares = crear_pares(lista)
    total_suma = sum(solo_pares)
    return(total_suma)
resultado = (sumar_pares_lista(lista=lista_jiiji))
print(resultado)