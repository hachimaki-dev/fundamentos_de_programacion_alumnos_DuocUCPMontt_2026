clave = "9182"
intentos_fallidos = 0
while True:
    if intentos_fallidos == 3:
        print("Bloqueo de tarjeta")
        break
    imput = input()
    if clave != imput:
        intentos_fallidos += 1
    elif imput == clave:
        print("Pase usted, buen senior")
        break