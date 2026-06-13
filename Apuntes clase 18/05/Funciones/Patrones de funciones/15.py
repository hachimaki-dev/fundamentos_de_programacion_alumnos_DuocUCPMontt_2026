def contar_aprobados_v1(lista):
    contador = 0
    for est in lista:
        if est["aprobado"] == True:
            contador = contador + 1
    return contador