from random import randint

limite_inferior = int(input("Ingrese su limite inferior: "))
limite_superior = int(input("Ingrese su limite superior: "))

numero = randint(limite_inferior,limite_superior)

ajustado = (numero // 4) * 4

if numero == 0:
    numero = 4

print("---- Adivina el multiplo de 4 ----")

for i in range(3):
    intento = int(input(f"\nIntento {i+1}/3: "))
    
    if intento == numero:
        print("¡Exacto! ¡Ganaste!")
        break
    elif intento < numero:
        print("Es más alto.")
    else:
        print("Es más bajo.")
else:
    print(f"\nSe acabaron los intentos. El número era {numero}.")