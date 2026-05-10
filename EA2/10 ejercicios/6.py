'''Desarrolle un programa que solicite dos números enteros para definir un rango. Luego genere un número aleatorio dentro del rango y lo ajuste para que sea par.

Reglas:

    Si el número generado es impar y numero + 1 sigue dentro del rango, usar numero + 1.
    Si numero + 1 se sale del rango, usar numero - 1.
    Si ya es par, no modificar.

El jugador tendrá 3 intentos para adivinar el número.

    Intento 1: indicar si el número es mayor o menor.
    Intento 2: además entregar pista de cercanía.
    Intento 3: si falla, mostrar el número y terminar.

Debe usar randint().'''

import random

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero_aleatorio = random.randint(numero1, numero2)
intentos = 0

if numero_aleatorio % 2 != 0:
    if numero_aleatorio + 1 <= numero2:
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
            elif num_ingresado - 2 or 3 != numero_aleatorio:
                print("estas cerca")
            else:
                print("estas un poco lejos")
        elif numero_aleatorio > num_ingresado:
            print("El numero es mayor")
            if num_ingresado + 1 == numero_aleatorio:
                print("estas muy cerca")
            elif num_ingresado + 2 or 3 != numero_aleatorio:
                print("estas cerca")
            else:
                print("estas un poco lejos")
    
    else:
        print(f"no pudiste adivinar. El numero era: {numero_aleatorio}")