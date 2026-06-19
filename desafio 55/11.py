
intentos_fallidos = 0

clave_ingresada = "admin123"

clave_correcta = "secreto"

if clave_ingresada == clave_correcta:
    print("entraste")
else:
    intentos_fallidos += 1
    print(f"intentos fallidos: {intentos_fallidos}")

