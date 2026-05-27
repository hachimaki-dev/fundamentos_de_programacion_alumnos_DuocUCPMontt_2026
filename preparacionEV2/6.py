#Desarrolle un programa que solicite dos números enteros para definir un rango. Luego genere un número aleatorio dentro del rango y lo ajuste para que sea par.

#Reglas:

#Si el número generado es impar y numero + 1 sigue dentro del rango, usar numero + 1.
#Si numero + 1 se sale del rango, usar numero - 1.
#Si ya es par, no modificar.
#El jugador tendrá 3 intentos para adivinar el número.

#Intento 1: indicar si el número es mayor o menor.
#Intento 2: además entregar pista de cercanía.
#Intento 3: si falla, mostrar el número y terminar.
#Debe usar randint().
from random import randint
numero_inicial = int(input("ingrese el primer numero"))
numero_final = int(input("ingrese el ultimo numero"))
numero = randint(numero_inicial, numero_final)
intentos = 3
diferencia = 0
if numero %2 != 0 :
    if numero + 1 <= numero_final:
        numero += 1
    else:
        numero -= 1
while intentos > 0 :
    ingrese_numero = int(input("ingrese numero"))
    if ingrese_numero != numero:
        intentos -= 1
        if ingrese_numero > numero:
            print("el nummero es menor")
        elif ingrese_numero < numero:
            print("el numero es mayor")
        diferencia = abs(numero - ingrese_numero)
        if intentos == 2:
            print(f"te dare una pista el numero esta a {diferencia} numeros mas")
        elif intentos == 3:
            print(f"fallaste el numero es {numero}")
            break
    elif ingrese_numero == numero:
        print("felicidades era el numero")
        break

