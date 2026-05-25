import random

inicio = int(input('Escoque un numero bajo: '))
fin = int(input('Escoge un numero mas alto: '))

# NUMERO ALEATORIO

numero = random.randint(inicio, fin)

# Ajustar al múltiplo de 4 menor o igual
ajustado = (numero // 3) * 3

# Verificar si queda fuera del rango
if ajustado < inicio:
    ajustado = inicio

    # Intentos
intento = 1

while intento <= 3:

    adivinanza = int(input())

    # Si adivina
    if adivinanza == ajustado:
        print("Felicitaciones, pudiste adivinar.")
        break

    # Pistas
    else:

        if adivinanza < ajustado:
            print("El número es mayor.")
        else:
            print("El número es menor.")

    # Último intento
    if intento == 3 and adivinanza != ajustado:
        print("Perdiste. El número era", ajustado)

    intento = intento + 1