import random

lim_inferior = ""

while not lim_inferior.isnumeric():
    lim_inferior = input("Limite inferior: ")

    if not lim_inferior.isnumeric():
        print("Ingrese un número entero")

lim_superior = ""

while not lim_superior.isnumeric():
    lim_superior = input("Limite superior: ")

    if not lim_superior.isnumeric():
        print("Ingrese un número entero")

lim_inferior = int(lim_inferior)
lim_superior = int(lim_superior)

num_aleatorio = random.randint(lim_inferior, lim_superior)

if num_aleatorio % 2 == 1:
    if num_aleatorio + 1 <= lim_superior:
        num_aleatorio += 1
    else:
        num_aleatorio -= 1

print("Adivina el número\nIngresa tu número para adivinar")

intentos_max = 3
intento = 1
acertado = False

while intento <= intentos_max and not acertado:
    numero = int(input(f"Intento {intento}: "))

    if num_aleatorio == numero:
        print("Felicitaciones, pudiste adivinar.")
        acertado = True
    elif intento == 1 or intento == 2:
        if num_aleatorio > numero:
            print(f"Pista: El número a adivinar es mayor que {numero}")
        else:
            print(f"Pista: El número a adivinar es menor que {numero}")
    else:
        print(f"No acertaste, el número era: {num_aleatorio}")
    
    intento += 1