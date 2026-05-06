contador_intentos = 0
clave = 123


while True:
    contador_intentos = contador_intentos + 1
    if contador_intentos >3:
        print("Bloqueo de Tarjeta")
        break