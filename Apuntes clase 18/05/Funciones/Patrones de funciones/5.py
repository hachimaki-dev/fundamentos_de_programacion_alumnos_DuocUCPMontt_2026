def buscar_posicion(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i  # encontramos! salimos inmediatamente
    return -1  # si el for terminó sin encontrar nada

def buscar_posicion_v2(lista, valor_buscado):
    for indice, valor in enumerate(lista):
        if valor == valor_buscado:
            return indice
    return -1