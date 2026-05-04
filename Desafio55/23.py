intentos_fallidos = 0
clave = "123"
clave_ingresada = "abc"


while True:
    if clave != clave_ingresada:
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        break

print("Bloque de tarjeta")