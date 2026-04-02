num_secreto = 14
respuesta = 0
contador_turnos = 0

while respuesta != num_secreto:
    respuesta = int(input("Ingresa un número: "))

    if respuesta < num_secreto:
        print("El número secreto es más ALTO")
    elif respuesta > num_secreto:
        print("El número secretro es más BAJO")

    contador_turnos += 1

print(f"¡Ganaste!, te tomó {contador_turnos} turnos adivinar")