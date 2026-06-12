def sumarPrint(a, b):
    print(a + b)   #solo IMPRIME, no entrega nada
    
def sumarReturn(a, b):
    return a + b   #ENTREGA el resultado

resultado1 = sumarPrint(3, 4)  #En pantalla 7
print(resultado1)   #En pantalla NONE

resultado2 = sumarReturn(3, 4)
print(resultado2)  #EN pantalla 7
