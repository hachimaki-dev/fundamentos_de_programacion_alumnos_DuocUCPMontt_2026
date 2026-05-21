#Crea promedio(lista) que retorne el promedio de una lista de números. Retorna 0 si la lista está vacía.

def promedio(lista):
    if len(lista) == 0:
        return 0
    
    suma = 0

    for numero in lista:
        suma += numero
    return suma / len(lista)

print(promedio([2, 5, 6, 8]))