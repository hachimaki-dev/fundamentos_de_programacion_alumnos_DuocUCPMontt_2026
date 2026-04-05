numero_ganador= 19
intentos=0
numero_usuario= None
while numero_usuario != numero_ganador:
    numero_usuario= int(input("Ingrese un número: "))
    if numero_usuario>numero_ganador:
        print("El número secreto es más BAJO")
        intentos+= 1
    elif numero_usuario<numero_ganador:
        print("El número secreto es más ALTO")
        intentos+= 1
print(f"¡Ganaste en {intentos} intentos!.")