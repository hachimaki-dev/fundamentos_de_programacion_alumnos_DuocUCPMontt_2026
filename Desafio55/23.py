intentos_fallidos=0
clave_secreta="Aloha"
clave_ingresada="Aloho"
while True:
    if clave_ingresada!=clave_secreta:
        intentos_fallidos+=1
        if intentos_fallidos>=3:
            print("Bloqueo de tarjeta")
            break