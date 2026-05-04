intentos_fallidos = 0
clave = "secreto"
clave_mala = "admin123"

if clave_mala == clave :
    print("entraste")
else :
    intentos_fallidos += 1

print (f"Intentos Fallidos {intentos_fallidos}")