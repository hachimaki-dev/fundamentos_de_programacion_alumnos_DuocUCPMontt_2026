def dupe_print(numero):
    print(numero * 2)
def dupe_return(numero):
    return numero * 2

a = dupe_print(5)   #Al no tener un return, devuelve None, en cambio, al tener Return devuelve el producto de la multiplicación.
b = dupe_return(5)
print(f" {a} | {b}")