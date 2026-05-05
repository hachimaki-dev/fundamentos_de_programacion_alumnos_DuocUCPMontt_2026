intentos_fallidos = 0 
clave_escrita = "admin123"
clave_correcta = "secreto"


if clave_escrita == clave_correcta:
    print("ENTRASTE")
else:
    intentos_fallidos += 1
    print("intentos fallidos: " + str(intentos_fallidos))    