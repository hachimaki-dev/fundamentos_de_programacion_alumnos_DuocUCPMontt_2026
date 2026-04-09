print("Adivina el numero secreto")

numero_secreto = 8
numero_elegido = 0
intentos = 0

while numero_secreto != numero_elegido :
    numero_elegido = int(input("Ingresa un numero del 1 al 10"))
    intentos +=1

    if numero_elegido < numero_secreto :
        print("El numero secreto es MAS ALTO")
        print(f"Intento nro {intentos}")
    elif numero_elegido > numero_secreto :
        print("El numero secreto es MAS BAJO")
        print(f"Intento nro {intentos}")
    else:
        print("El numero elegido es el correcto")
        print(f"Ganaste en {intentos} intentos")


    