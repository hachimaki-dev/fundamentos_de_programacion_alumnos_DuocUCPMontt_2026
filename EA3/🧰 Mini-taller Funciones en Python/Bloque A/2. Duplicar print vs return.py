def duplicar_print(numero):
    print(numero * 2)

def duplicar_return(numero):
    return numero * 2

a = duplicar_print(5)
b = duplicar_return(5)

print(a)
print(b)

#donde duplicar_print no tiene un return devuelve none a diferencia del return que si coloca solo 10 