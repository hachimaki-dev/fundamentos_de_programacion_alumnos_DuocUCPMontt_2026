número_secreto = 46
contador = 0

número_elegido = int(input("elige un número aleatorio : "))
while número_elegido != número_secreto :
    print("Número elegido incorrecto")
    contador = contador + 1

    if número_elegido > número_secreto :
        print("El número secreto es más BAJO")
    elif número_elegido < número_secreto :
        print("El número secreto es más ALTO")
        
    número_elegido = int(input("Elige nuevamente : "))

contador = contador + 1
print(f"¡Ganaste en {contador} intentos!")

