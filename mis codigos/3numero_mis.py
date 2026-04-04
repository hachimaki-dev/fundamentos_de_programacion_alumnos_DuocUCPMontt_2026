print("=== A jugar con Numeros ===")

numero_secreto = 42
intentos = 0

numero_usuario = int(input("Adivina el número secreto: "))

while numero_usuario != numero_secreto:
    intentos = intentos + 1

    if numero_usuario < numero_secreto:
        print("El número secreto es más ALTO")
    elif numero_usuario > numero_secreto:
        print("El número secreto es más BAJO")

    numero_usuario = int(input("Intenta nuevamente: "))

intentos = intentos + 1

print("¡Ganaste en", intentos, "intentos!")