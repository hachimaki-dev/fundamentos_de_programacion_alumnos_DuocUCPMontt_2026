print("Calculadora \n '+':Sumar \n '-':Restar \n '*':Multiplicar \n '/':Dividir")
numero1 = int(input("Ingresa el primer número"))
simbolo = str(input("ingresa el signo de operación"))
numero2 = int(input("Ingresa el segundo número"))

if(simbolo == "+"):
    print(numero1 + numero2)
elif(simbolo == "-"):
    print(numero1 - numero2)
elif(simbolo == "*"):
    print(numero1 * numero2)
elif(simbolo == "/"):
    print(numero1 / numero2)
else:
    print("operacion no valida")
    