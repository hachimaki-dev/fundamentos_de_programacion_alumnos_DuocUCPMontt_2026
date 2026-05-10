import random


inicio = int(input("Ingresa el número inicial del rango: "))
fin    = int(input("Ingresa el número final del rango: "))


numero   = random.randint(inicio, fin)
ajustado = (numero // 3) * 3


if ajustado < inicio:
    ajustado = inicio


for intento in range(1, 4):
    guess = int(input("Adivina: "))

    if guess == ajustado:
        print("Felicitaciones, pudiste adivinar.")
        break

  
    if guess < ajustado:
        print("El número es mayor.")
    else:
        print("El número es menor.")


    if intento == 2:
        diferencia = abs(ajustado - guess)
        if diferencia <= 2:
            print("Estás muy cerca.")
        else:
            print("Estás lejos.")

    if intento == 3:
        print(f"El número era {ajustado}.")