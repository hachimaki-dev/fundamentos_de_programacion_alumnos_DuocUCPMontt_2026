contador_intento_fallidos = 0
maximo_intentos = 3
while True:
    contador_intento_fallidos += 1
    
    if contador_intento_fallidos >= maximo_intentos:
        print(contador_intento_fallidos , maximo_intentos)
        break