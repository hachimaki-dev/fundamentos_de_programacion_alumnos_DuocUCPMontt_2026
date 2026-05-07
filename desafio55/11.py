intentos_fallidos = 0
clave_correcta = "secreto"
clave_ingresada = "admin123"

if clave_ingresada == clave_correcta:
    print("entraste")
else: 
    intentos_fallidos += 1
    print("intentos fallidos: " + str(intentos_fallidos))



