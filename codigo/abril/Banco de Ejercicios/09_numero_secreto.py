numero_secreto = 42
respuesta_usuario = 0
contador_intentos = 0

while respuesta_usuario != numero_secreto:
    contador_intentos += 1
    respuesta_usuario = int(input(f"Intento {contador_intentos}. Ingresa un número: "))

    if respuesta_usuario < numero_secreto:
        print("El número secreto es más ALTO.")
    elif respuesta_usuario > numero_secreto:
        print("El número secreto es más BAJO.")
    else:
        break # break para mayor legibilidad, el bucle debería romperse antes

print(f"¡Respuesta correcta! Adivinaste el número en {contador_intentos} intentos.")
