def buscar_posicion(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def eliminar(lista, valor):
    posicion = buscar_posicion(lista, valor)  # reutilizamos
    if posicion != -1:
        lista.pop(posicion)
        print("Eliminado correctamente")
    else:
        print("No se encontró el elemento")