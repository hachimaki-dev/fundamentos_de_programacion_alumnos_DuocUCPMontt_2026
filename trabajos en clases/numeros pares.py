numero = int(input("ingrese un numero: "))

if numero % 2 != 0:   # SI el número es impar...
    numero += 1        # ...entonces súmale 1
print(numero)

# Actuar cuando es PAR (y no hacer nada si es impar)
if numero % 2 == 0:
    print("es par, hago algo")