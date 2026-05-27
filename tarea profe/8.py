def filtrar_pares(listas_numeros):
    lista_pares = []
    for i in listas_numeros:
        if i %2 == 0:
            lista_pares.append(i)
    return print(lista_pares)        
listadenumeros = [23,32,43,33,44,12,9,3,4,2]
filtrar_pares(listadenumeros)