from random import randint

limite_inferior = int(input("Ingrese su limite inferior: "))
limite_superior = int(input("Ingrese su limite superior: "))

numero = randint(limite_inferior,limite_superior)

ajustado = (numero// 3) * 3

if numero == 0:
    numero = 3

print("--- Adivina el multiplo de 3 ---")

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