secret_number = 23

print("Bienvenido al programa para acceder a una copia gratuita de gta 6")
print("Si logra adivinar el número, se llevara una copia exclusiva.")

rounds_counter = 1

respuesta = int(input("Ingrese el número secreto: "))

while respuesta != secret_number:
    if respuesta > secret_number:
        print("El número ingresado es mayor al requerido.")
        rounds_counter = rounds_counter + 1
    elif respuesta < secret_number:
        print("El número ingresado es menor al requerido.")
        rounds_counter = rounds_counter + 1

    respuesta = int(input("Vuelva a ingresar el número: "))

print("Has acertado")
print(f"Has ganado en {rounds_counter} intento/s")