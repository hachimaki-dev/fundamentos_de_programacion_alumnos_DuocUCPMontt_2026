#Crea promedio(lista) que retorne el promedio de una lista de números. Retorna 0 si la lista está vacía.

def promedio(lista: list=[]):
    total=0
    for i in lista:
        total+=i
    if len(lista) > 0:
        promedio = total/(len(lista))
    else: 
        promedio = 0
    return promedio    

resultado= promedio([43,52,6,3,23,2,31,4])

print (resultado)
