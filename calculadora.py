#Tarea Andrew y Sider


print ("Bienvenido a calculadora 2000")

continuar = True

print ("Ingrese el primer numero")
num1 = int(input())
print ("Ingrese el segundo numero")
num2 = int(input())

while continuar :

    print ("Ingrese la operacion a realizar o 0 para salir")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Division")
    print ("0. Salir")
    operacion = int(input())
    if operacion == 1 :
        print (f"El resultado es {num1 + num2}")
        break
    elif operacion == 2 :
        print (f"El resultado es {num1 - num2}")
        break
    elif operacion == 3 :
        print (f"El resultado es {num1 * num2}")
        break
    elif operacion == 4 :
        print (f"El resultado es {num1 / num2}")
        break