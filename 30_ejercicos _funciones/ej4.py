def mayor_de_tres(a, b, c):
    if a >= b and a >= c: 
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
nummero_a = int(input("ingresa el primer numero: "))
nummero_b = int(input("ingresa el sgungo numero: "))
nummero_c = int(input("ingresa el tercer numero: "))
resultado = mayor_de_tres(a = nummero_a, b = nummero_b, c = nummero_c)
print(resultado)