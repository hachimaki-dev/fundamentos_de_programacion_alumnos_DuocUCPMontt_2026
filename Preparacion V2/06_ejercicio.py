import random

# Pedir rango
inicio = int(input('escoje un rango bajo: '))
fin = int(input('Esco un ralgo mas altoa: '))

# Número aleatorio
numero = random.randint(inicio, fin)

# Ajustar para que sea par
if numero % 2 != 0:

    if numero + 1 <= fin:
        numero = numero + 1

    else:
        numero = numero - 1

# Variable de intentos
intento = 1

# Ciclo while
while intento <= 3:

    adivinanza = int(input('usuario: '))

    # Si adivina
    if adivinanza == numero:
        print("Felicitaciones, pudiste adivinar.")
        break

    # Intento 1
    elif intento == 1:

        if adivinanza < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

    # Intento 2
    elif intento == 2:

        if adivinanza < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        diferencia = abs(adivinanza - numero)

        if diferencia <= 2:
            print("Estás cerca.")
        else:
            print("Estás lejos.")

    # Intento 3
    else:
        print("Perdiste. El número era", numero)

    # Aumentar intento
    intento = intento + 1