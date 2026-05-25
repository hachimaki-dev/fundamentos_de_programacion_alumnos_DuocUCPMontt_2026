import random
numero1 = int(input("Eligue el 0: "))
numero2 = int(input("Eligue un numero: "))
contador_intentos = 0
opcion_user = -1

numero_secreto = random.randint(numero1, numero2)

if numero_secreto % 2 != 0:
    if numero_secreto + 1 <= numero2:
        numero_secreto += 1
    else:
        numero_secreto -= 1
while opcion_user != numero_secreto:
    opcion_user = int(input("Adivina el numero del programa: "))
    contador_intentos += 1
    if opcion_user == numero_secreto:
            print("Felicitaciones, pudiste adivinar.")
            break
        
    elif contador_intentos == 1:
        if opcion_user < numero_secreto:
            print("El numero es mayor")
        else:
            print("El numero es menor")

    elif contador_intentos == 2:
        if opcion_user < numero_secreto:
            print("El numero es mayor")
        else:
            print("El numero es menor")
        print(f"El numero esta cerca del: {numero_secreto - 1}")
            
    elif contador_intentos == 3:
        print(f"Fin del juego, el numero secreto es: {numero_secreto}")
        break