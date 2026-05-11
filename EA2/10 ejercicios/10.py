'''Desarrolle un programa que solicite dos números enteros para definir un rango. Luego genere un número aleatorio dentro del rango y lo ajuste para que sea impar.

Reglas:

    Si el número generado es par y numero + 1 sigue dentro del rango, usar numero + 1.
    Si numero + 1 se sale del rango, usar numero - 1.
    Si ya es impar, no modificar.

El jugador tendrá 3 intentos para adivinar el número.

    Intento 1: indicar si el número es mayor o menor.
    Intento 2: además entregar pista de cercanía.
    Intento 3: si falla, mostrar el número y terminar.

Debe usar randint().'''

import random

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
limite_inf = min(numero1, numero2)
limite_sup = max(numero1, numero2)
numero_aleatorio = random.randint(limite_inf, limite_sup)
intentos = 0


if numero_aleatorio % 2 == 0:
    if numero_aleatorio + 1 <= limite_sup:
        numero_aleatorio += 1
    else:
        numero_aleatorio -= 1

while intentos < 3:
    num_ingresado = int(input("Adivina el numero: "))
    intentos += 1
    if num_ingresado == numero_aleatorio:
        print("Felicitaciones, pudiste adivinar.")
        break
    
    elif intentos == 1 and num_ingresado != numero_aleatorio:
        if numero_aleatorio < num_ingresado:
            print("El numero es menor")
        else:
            print("el numero es mayor")
    
    elif intentos == 2 and num_ingresado != numero_aleatorio:
        if numero_aleatorio < num_ingresado:
            print("El numero es menor")
            if num_ingresado - 1 == numero_aleatorio:
                print("estas muy cerca")
            elif num_ingresado - 2 != numero_aleatorio or num_ingresado - 3 != numero_aleatorio:
                print("estas cerca")
            else:
                print("estas un poco lejos")
        elif numero_aleatorio > num_ingresado:
            print("El numero es mayor")
            if num_ingresado + 1 == numero_aleatorio:
                print("estas muy cerca")
            elif num_ingresado + 2 != numero_aleatorio or num_ingresado + 3 != numero_aleatorio:
                print("estas cerca")
            else:
                print("estas un poco lejos")
    
    else:
        print(f"no pudiste adivinar. El numero era: {numero_aleatorio}")