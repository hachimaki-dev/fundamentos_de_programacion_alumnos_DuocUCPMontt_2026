from random import randint 

numero1 = int(input("Ingrese el PRIMER numero/ limite inferior(debe de ser menor que el segudo numero que vaya a colocar) : "))
numero2 = int(input("Ingrese el SEGUNDO numero/ limite superior (debe de ser menor que el segudo numero que vaya a colocar) : "))
print()
numero = randint(numero1,numero2)

if numero % 2 != 0:
    if numero + 1 <= numero2:
        numero += 1
    else:
        numero -= 1
     


intentos = 3

while True:
    intento1 = int(input("Intente adivinar el numero(Tienes 3 intentos) : "))
    intentos -= 1
    if intentos <= 0:
        print("Perdiste ")
        print(f"el numero era {numero}")
        break
    
    if intento1 == numero:
        print("Felicitaciones , pudiste adivinar")
        break
    
    if intento1 < numero:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    
    intento2 = int(input("Intente de nuevo (segundo intento) :   "))
    intentos -= 1
    if intentos <= 0:
        print("Perdiste ")
        print(f"el numero era {numero}")
        break

    if numero > intento1:
        distancia1 = numero - intento1
    else:
        distancia1 = intento1 - numero

    if numero > intento2:
        distancia2 = numero - intento2
    else:
        distancia2 = intento2 - numero


    if intento2 == numero:
        print("Felicitaciones , pudiste adivinar")
        break
    
    if intento2 < numero:
        print("El numero es mayor")
        if distancia1 < distancia2:
             print("Te Dare una Pista : \n")
             print(f"Estuviste mas cerca en el primer intento )")
             print()
        else:
             print("Te Dare una Pista : \n")
             print(f"Estuviste más cerca en el segundo intento ")
             print()
    else:
        print("El numero es menor")
        if distancia1 < distancia2:
             print("Te Dare una Pista : \n")
             print(f"Estuviste mas cerca en el primer intento )")
             print()
        else:
             print("Te Dare una Pista : \n")
             print(f"Estuviste más cerca en el segundo intento ")
             print()

    intento3 = int(input("Intente de nuevo (Ultimo intento) :   "))
    intentos -= 1
    if intentos <= 0:
        print("Perdiste ")
        print(f"el numero era {numero}")
        break

    if intento3 == numero:
        print("Felicitaciones , pudiste adivinar")
        break
    
    if intento3 < numero:
        print("El numero es mayor")
    else:
        print("El numero es menor")
        
