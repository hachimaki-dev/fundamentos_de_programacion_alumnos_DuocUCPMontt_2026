import random

#limites
limite_inf = 0
limite_sup = 10

#numeor aleatorio
numero = random.randint(limite_inf, limite_sup) #Numero aleatorio 
ajustado = (numero // 3) * 3 #Numero ajustado para ser multiplo de 3

#condiciones
if ajustado < limite_inf:
    ajustado = limite_inf

print(f"Se generó un número enntre {limite_inf} y {limite_sup}\n¿Podrás adivinarlo?")

#Intentos para 
win = False

for intento in range(1, 4):
    print(f"\nIntento {intento}/3")
    respuesta = int(input("Ingresa un número: "))

    #juego
    if respuesta == ajustado:
        print("\n----------------------------------")
        print("Felicitaciones, pudiste adivinar")
        print("-----------------------------------\n")
        win = True
        break
    elif respuesta < ajustado:
        print("\nEs mayor")
    else:
        print("\nEs menor")

if not win:
    print("Fallaste :(")
    print("\n-------------------------")
    print(f"El número era: {ajustado}")
    print("-------------------------\n")