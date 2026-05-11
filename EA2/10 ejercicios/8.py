'''Desarrolle un programa que genere un número aleatorio dentro de un rango y luego lo ajuste al múltiplo de 3 inmediatamente menor o igual.

Debe utilizar: ajustado = (numero // 3) * 3

Si el número ajustado queda fuera del rango, debe usar el límite inferior.

El usuario tendrá 3 intentos para adivinar el número.'''


import random

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
limite_inf = min(numero1, numero2)
limite_sup = max(numero1, numero2)
numero_aleatorio = random.randint(limite_inf, limite_sup)
ajustado = (numero_aleatorio // 3) * 3

if ajustado < limite_inf:
    ajustado = limite_inf
intentos = 0

while intentos < 3:
    num_ingresado = int(input("Adivina el numero: "))
    intentos += 1
    
    if num_ingresado == ajustado:
        print("Felicitaciones, pudiste adivinar.")
        break
    elif intentos == 3:
        print(f"Lo siento, el numero era {ajustado}.")
    else:
        if ajustado < num_ingresado:
            print("El numero es menor")
        else:
            print("El numero es mayor")