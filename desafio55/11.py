intentos_fallidos = 0
clave_escrito = 'Admin123'
clave_correcta = 'secreto'
if clave_escrito == clave_correcta:
    print("Entraste")
else :
    intentos_fallidos = intentos_fallidos + 1
    print(f" intentos fallidos:{intentos_fallidos}")
