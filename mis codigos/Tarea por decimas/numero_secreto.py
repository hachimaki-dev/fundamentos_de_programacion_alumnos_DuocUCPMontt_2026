numero_secreto = 7
numero_intentos = 0
intentos_user = 0
print("¡Bievenido a este juego! Adivina el número secreto para ganar")

while intentos_user != numero_secreto:
    intentos_user = int(input("Ingresa un numero entre el 1 y el 10: "))
    numero_intentos += 1
    if intentos_user > numero_secreto:
        print("el numero secreto es mas BAJO")
    elif intentos_user < numero_secreto:
        print("El numero secreto es mas ALTO")
    
print(f"¡Bien hecho! Ganaste en {numero_intentos} intentos")