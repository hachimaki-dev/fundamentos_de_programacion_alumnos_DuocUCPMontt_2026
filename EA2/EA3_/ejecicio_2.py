from random import randint

limite_inferior = int(input("Ingrese limite inferior: "))
limite_superior = int(input("Ingrese limite superior: "))

intentos_maximo = 3

numero = randint(limite_inferior, limite_superior)

adivinando_numero = int(input("Adivina el numero: "))

while adivinando_numero != numero and intentos_maximo > 1:

    if adivinando_numero == numero:
        print("Felicitaciones, pudiste adivinar")

    elif adivinando_numero > numero:
        print("El numero es menor")

    elif adivinando_numero < numero:
        print("El numero es mayor")

    intentos_maximo -= 1

    print("Intentos restantes:", intentos_maximo)

    adivinando_numero = int(input("Adivina el numero: "))

if adivinando_numero == numero:
    print("Felicitaciones, pudiste adivinar")

else:
    print(f"Perdiste, el numero era: {numero}")
    