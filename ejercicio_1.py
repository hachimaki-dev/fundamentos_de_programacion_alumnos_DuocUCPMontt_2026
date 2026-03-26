# Crear diagrama de flujos del algoritmo solicitado solo cuando mi diagrama de flujos ha sido validado, entonces, crear codigo
#1 Crear un algoritmo que oblige al usuario a adivinar un numero secreto previamente determinado por el sistema. si falla indicarle que fallo y solicitarle que vuelva intertarlo. si acierta, lo felicitamos y termina el programa.

import random

numero_secreto = random.randint(1, 10)
numero_adivinado = 0

print(numero_secreto)

while numero_secreto != numero_adivinado:
    numero_adivinado = int(input("Ingrese un numero para adivinar (Entre el 1-10): "))
    if numero_adivinado != numero_secreto:
        print("Fallaste! Intente denuevo!")


print("Has ganado!")

            