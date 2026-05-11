'''Desarrolle un programa que genere un número aleatorio dentro de un rango y luego lo ajuste al múltiplo de 4 inmediatamente menor o igual.

Debe utilizar: ajustado = (numero // 4) * 4

Si el número ajustado queda fuera del rango, debe usar el límite inferior.

El usuario tendrá 3 intentos para adivinar el número.'''

import random

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero_aleatorio = random.randint(min(numero1, numero2), max(numero1, numero2))
ajustado = (numero_aleatorio // 4) * 4
intentos = 0
limite_inf = min(numero1, numero2)
limite_sup = max(numero1, numero2)

if ajustado < limite_inf:
    ajustado = limite_inf
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
            
