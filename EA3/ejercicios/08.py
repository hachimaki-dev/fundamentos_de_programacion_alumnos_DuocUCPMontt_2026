#Crea filtrar_pares(lista_numeros) que reciba una lista, y retorne una NUEVA lista solo con los números pares.
def filtrar_pares(lista_numeros: list):
    lista_pares=[]
    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares
            
resultado = filtrar_pares([2,3,6,3,5,2,7,8])            

print(resultado)