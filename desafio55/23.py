intentos_fallidos = 0
clave_correcta = 55646

while True:
    clave = int(input("¿Cual es la clave?"))
    if clave != clave_correcta: 
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Bloqueo de Tarjeta")
        break