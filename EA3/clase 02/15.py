#Usando filtrar_pares() y sumar(), crea sumar_pares_lista(lista) que reciba una lista y retorne la suma de todos los números pares en ella.

def filtrar_pares(lista):
    return [numero for numero in lista if numero % 2 == 0]

def suma(lista):
    return sum(lista)

def sumar_pares_lista(lista):
    pares = filtrar_pares(lista)
    return suma(pares)

numeros = [1, 2, 3, 4, 5, 6]

print(sumar_pares_lista(numeros))