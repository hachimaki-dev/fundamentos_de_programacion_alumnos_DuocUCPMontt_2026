#Crea filtrar_pares(lista_numeros) que reciba una lista, y retorne una NUEVA lista solo con los números pares.

def filtrar_pares(lista_numeros):
    numeros_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
    return numeros_pares
    
par = filtrar_pares([1, 2, 3, 4, 5, 6])
print(par)
#output [2, 4, 6]
