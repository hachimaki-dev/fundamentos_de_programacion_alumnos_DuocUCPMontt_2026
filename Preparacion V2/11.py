                   
import random

# Pedir rango
rango1 = int(input("Ingrese un número: "))
rango2 = int(input("Ingrese otro número: "))

# Crear número aleatorio
numero = random.randint(rango1, rango2)

# Convertir a impar si sale par
if numero % 2 == 0:

    if numero + 1 <= rango2:
        numero += 1
    else:
        numero -= 1

# Contador de intentos
intentos = 0

# Juego
while intentos < 3:

    adivinanza = int(input("Adivina el número secreto: "))

    # Si acierta
    if adivinanza == numero:
        print("¡Adivinaste, felicidades!")
        break

    # Si falla
    else:
        print("Ups, ese no es")
        intentos += 1

    # Primera pista
    if intentos == 1:

        if adivinanza > numero:
            print("El número secreto es menor")

        else:
            print("El número secreto es mayor")

    # Segunda pista
    elif intentos == 2:

        diferencia = abs(numero - adivinanza)

        print(f"Estás a {diferencia} números de distancia")

    # Perder
    elif intentos == 3:

        print(f"No pudiste adivinar")
        print(f"El número secreto era: {numero}")