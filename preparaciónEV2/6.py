import random

inicio = int(input("Ingresa el número inicial del rango: "))
fin = int(input("Ingresa el número final del rango: "))

numero = random.randint(inicio, fin)

if numero % 2 != 0:
    if numero + 1 <= fin:
        numero += 1
    else:
        numero -= 1

for intento in range(1, 4):
    guess = int(input("Adivina: "))

    if guess == numero:
        print("Felicitaciones, pudiste adivinar.")
        break

    if guess < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    if intento == 2:
        diferencia = abs(numero - guess)
        if diferencia <= 2:
            print("Estás muy cerca.")
        else:
            print("Estás lejos.")

    if intento == 3:
        print(f"El número era {numero}.")