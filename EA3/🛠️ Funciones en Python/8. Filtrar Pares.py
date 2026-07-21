#Crea filtrar_pares(lista_numeros) que reciba una lista, y retorne una NUEVA lista solo con los números pares.

def filtra_pares(lista):

    lista_pares = []

    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)

    return lista_pares


print(filtra_pares([1, 2, 3, 4, 5, 6]))