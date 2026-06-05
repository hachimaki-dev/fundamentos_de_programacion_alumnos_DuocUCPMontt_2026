def filtrar_pares(lista_numeros: list):
    lista_pares = []
    for i in lista_numeros:
        if i %2 == 0:
            lista_pares.append(i)
        return lista_pares   
        