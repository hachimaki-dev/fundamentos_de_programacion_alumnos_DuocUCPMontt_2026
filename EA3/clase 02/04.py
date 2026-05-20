#Crea mayor_de_tres(a, b, c) que reciba 3 números y retorne el mayor de ellos.

def mayor_de_tres(a, b, c):
    if b < a > c:
        return a
    elif a < b > c:
        return b
    elif b < c > a:
        return c 

numero_mayor = mayor_de_tres(45, 4, 5)
print(numero_mayor)