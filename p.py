from random import randint
num1 = int(input("Ingrese el limite inferior (Recomendacion: 1): "))
num2 = int(input("ingrese el limite superior (Recomendacion: 10): "))
ingresar = int(input("Tu numero: "))
contador = 0
numero = randint(num1, num2) 
while contador <4:
    contador = contador + 1
    print(f"Intentos: {contador}")
    print("¡Recuerda! Tienes 3 intentos...")
    pista = num2 - ingresar
    if contador == 4:
        print("Perdiste...")
        print(f"El numero era {numero}")
        print(f"Intentos: {contador}")
        break
    if ingresar == numero:
        print(f"Felicidades! pudiste adivinar! En el intento: {contador}!")
        break
    if contador == 2:
        print("ULTIMO INTENTO")
        if contador == 2:
            print("Te dare una pista...")
            print(f"El numero esta cerca del {pista}...")
    if ingresar > numero:
        print("Tu numero es mayor.")
        if contador == 3:
            print("Perdiste...")
            print(f"El numero era {numero}")
            print(f"Intentos: {contador}")
            break
        else:
             ingresar = int(input("Tu numero: "))
    elif ingresar < numero:
        print("Tu numero es menor.")
        if contador == 3:
            print("Perdiste...")
            print(f"El numero era {numero}")
            print(f"Intentos: {contador}")
            break
        else:
            ingresar = int(input("Tu numero: "))