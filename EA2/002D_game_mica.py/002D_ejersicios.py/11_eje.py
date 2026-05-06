intentos_fallidos = 0
asume_clave = "Admin123"
clave_correcta = "secreto"

if asume_clave == clave_correcta:
    print("Entraste")
else:
    intentos_fallidos += 1
    print("Intentos fallidos: " + str(intentos_fallidos))
