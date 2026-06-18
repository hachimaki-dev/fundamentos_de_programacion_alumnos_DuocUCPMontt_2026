from random import randint

numero = randint(1, 10)

numero_final = numero + 1
numero_final = numero - 1

juguemos = input("Para jugar diga (SI): ")

if numero % 2 != 0:
    
    if numero + 1 <= numero:
        numero = numero + 1
    else:
        numero = numero - 2

    intento1 = int(input("Ingrese su numero: "))

    if intento1 == numero:
        print("Felicidades, adivinaste el numero")

    else:
        
        if intento1 < numero:
            print("El numero es mayor")
        else:
            print("El numero es menor")

        intento2 = int(input("Ingrese su nuevo numero: "))

        if intento2 == numero:
            print("Felicidades, adivinaste al segundo intento")

        else:

            if intento2 > numero:
                print(f"El numero es mayor que {intento2} y mayor que {intento1}")

            if intento2 < numero:
                print(f"El numero es menor que {intento2}")

            intento3 = int(input("Ultima oportunidad: "))

            if intento3 == numero:
                print("¡FELICIDADES! Adivinaste al tercer intento")

            else:
                print(f"Lamentablemente no era {intento3}, ni {intento2} ni {intento1}")
                print(f"El numero correcto era: {numero}")