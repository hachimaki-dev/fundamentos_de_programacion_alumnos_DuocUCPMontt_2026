#Usando filtrar_pares() y sumar(), crea sumar_pares_lista(lista) que reciba una lista y retorne la suma de todos los números pares en ella.

from ejercicio02 import sumar

from ejercicio08 import filtrar_pares

def sumar_pares_lista(lista):
    pares=filtrar_pares(lista)
    total=0
    for i in pares:
          total=sumar(total, i)
    return total

resultado = sumar_pares_lista([3,4,5,6,2])

print (resultado)