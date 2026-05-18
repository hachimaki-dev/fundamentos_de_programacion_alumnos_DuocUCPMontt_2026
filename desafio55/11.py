intentos_fallidos = 0
clave_correcta = "secreto"
clave_ingresada = "Admin123"
if clave_ingresada == clave_correcta:
    print("Entraste")
else:
    intentos_fallidos += 1
    print("Intentos fallidos: " + str(intentos_fallidos))