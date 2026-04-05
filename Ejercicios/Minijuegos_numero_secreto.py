numero_secreto = 42
intentos = 0
usuario_adivino = 0

print("--- ¡ADIVINA EL NÚMERO SECRETO! ---")

while usuario_adivino != numero_secreto:
    usuario_adivino = int(input("\nIntroduce un número: "))
    
    intentos = intentos + 1
    
    if usuario_adivino < numero_secreto:
        print("El número secreto es más ALTO")
    elif usuario_adivino > numero_secreto:
        print("El número secreto es más BAJO")

print(f"\n¡Ganaste en {intentos} intentos!")
