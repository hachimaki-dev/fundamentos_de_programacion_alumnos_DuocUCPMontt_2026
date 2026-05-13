from random import randint

limite_inferior = int(input("Ingrese su limite inferior: "))
limite_superior = int(input("Ingrese su limite superior: "))

numero = randint(limite_inferior,limite_superior)

if numero % 2 == 0:
    if numero + 1 < limite_superior:
        numero += 1
    else:
        numero -= 1

print("-- Adivina el numero impar --")

for i in range(3):
    intento = int(input(f"Intento {i+1}/3: "))

    if intento == numero:
        print("Ganaste")
        break

    elif intento < numero:
        print("Es mas alto")

    else:
        print("Es mas bajo")

else:
    print(f"Perdiste, el numero correcto era: {numero}")