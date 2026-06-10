from random import randint

numero1 = int(input("ingrese el limite inferior : "))
numero2 = int(input("ingresa el limite superior : "))



numero_aletorio = randint(numero1 , numero2)
if numero_aletorio % 2 != 0:

    if numero_aletorio + 1 > numero1 and numero_aletorio < numero2:
        numero_aletorio = numero_aletorio +1

    elif numero_aletorio + 1 < numero1 and numero_aletorio + 1  > numero2:
        numero_aletorio = numero_aletorio -1



while True:
    intento_1 = int(input(" adivina el numero aletorio : "))
    if intento_1 != numero_aletorio:

        if intento_1 > numero_aletorio:
            print("el numero a adivinar es menor")

        elif intento_1 < numero_aletorio:
            print("el numero a adivinar es mayor")

        else:
            print("felicidades lograste adivinar")
            break



    intento_2 = int(input(" adivina el numero aletorio : "))
    if intento_2 != numero_aletorio:

        if intento_2 > numero_aletorio:
            print("el numero a adivinar es menor")

        elif intento_2 < numero_aletorio:
            print("el numero a adivinar es mayor")
            

    elif intento_2 == numero_aletorio:
            print("felicidades lograste adivinar")
            break

    print("te dare un pista : ")
    pista_numero_mas_cerca1 = intento_1 - numero_aletorio
    pista_numero_mas_cerca2 = intento_2 - numero_aletorio
    
    if pista_numero_mas_cerca1 < pista_numero_mas_cerca2:
        print(f"el intento 1 estuvo mas cerca del numero secreto") 
                
    elif pista_numero_mas_cerca2 < pista_numero_mas_cerca1:
        print(f"el intento 2 estuvo mas cerca del numero secreto")



    intento_3 = int(input("adivina el numero aletorio : "))

    if intento_3 != numero_aletorio:
        print(f"perdiste , el numero era {numero_aletorio}")
        break
    elif intento_3 == numero_aletorio:
        print("felicidades lograste adivinar")
        break

