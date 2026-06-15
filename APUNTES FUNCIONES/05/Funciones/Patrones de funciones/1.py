def sumar_print(a, b):
    print(a + b)  # solo IMPRIME, no entrega nada

def sumar_return(a, b):
    return a + b  # ENTREGA el resultado

resultado1 = sumar_print(3, 4)   # en pantalla aparece "7"
print(resultado1)                # pero esto imprime "None" !!

resultado2 = sumar_return(3, 4)  # no aparece nada en pantalla
print(resultado2)                # esto imprime "7"