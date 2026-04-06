contador_intentos = 1
numero_secreto = 64
numero_usuario = 0
while numero_usuario != 64:
    numero_usuario = int(input("Escribe un numero: "))
    if numero_usuario <= 63:
        print("El numero secreto es más ALTO")
        contador_intentos = contador_intentos + 1
    elif numero_usuario >= 65:
        print("El numero secreto es más BAJO")
        contador_intentos = contador_intentos + 1
if numero_usuario == 64:
    print(f"¡Ganaste en {contador_intentos} intentos!")