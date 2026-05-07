intentos_fallidos = 0

while True:
    intento_correcto = False  # simulación de intento incorrecto

    if not intento_correcto:
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print('Bloqueo de Tarjeta')
        break