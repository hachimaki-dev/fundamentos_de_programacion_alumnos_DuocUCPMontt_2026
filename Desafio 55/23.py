contador_intentos = 0
maximo_intentos = 3

while True :
    contador_intentos += 1

    if contador_intentos >= maximo_intentos :
        print("Bloqueo de Tarjeta")
        break