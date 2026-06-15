def filtrar_pares(lista:list):
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par