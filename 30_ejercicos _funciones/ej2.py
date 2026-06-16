def sumar(a, b):
    return a + b
while True:
    try:
        numero1 = int(input("ingrese el n1 para sumar: "))
        numero2 = int(input("ingrese el n2 para sumar: "))
        break
    except ValueError:
        print("dato invalido intentalo nuevamente")
resultado = sumar(a = numero1, b = numero2)
print(resultado)