intentos_fallidos = 0
clave = 2929
while True:
    print("introdusca la clave")
    intento = int(input())
    if intento != clave:
        intentos_fallidos += 1
        print("vuelva intentarlo")
        if intentos_fallidos == 3:
            print("tarjeta bloqueda")
            break
    else:
        print("bienvenido")