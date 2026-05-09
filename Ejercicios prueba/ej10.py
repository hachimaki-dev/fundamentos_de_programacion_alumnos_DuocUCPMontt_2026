import random
#inputs de rango
print("---- Adivina el número ----\n")

inicio = int(input("Ingresa el inicio del rango a adivinar: "))
fin = int(input("Ingresa el fin del rango: "))

#numero aliatorio
numero = random.randint(inicio, fin)

#Reglas para adivinar
if numero % 2 == 0:
    if numero + 1 <= fin:
        numero += 1
    else:
        numero -= 1

print(f"Se escogió un número entre {inicio} y {fin}")
print("Tiene 3 intentos :D")

#Inicia el juego
for intento in range(1, 4):
    print(f"\n----------- Intento {intento}/3 -----------\n")
    respuesta = int(input("Ingresa un número: "))

    if respuesta == numero:
        print("\n----------- Felicitaciones, pudiste adivinar -----------")
        break
    
    if intento == 3:
        print("\n-------------------------")
        print(f"El número era: {numero}")
        print("-------------------------\n")
    elif intento < 3:
        if respuesta < numero:
            print(f"\nEl numero es mayor que {respuesta}")
        else:
            print(f"\nEl numero es menor que {respuesta}")
    
    if intento == 2:
        diferencia = abs(respuesta - numero)
        if diferencia <= 2:
            print("\nEstás muy cerca")
        elif diferencia <= 5:
            print("\nEstás cerca")
        elif diferencia <= 10:
            print("\nEstás a la mitad")
        else:
            print("\n¡Uy! Estás algo lejos")
    
print()