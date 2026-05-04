intentos_fallidos = 0

clave = "secreto"
calve_ingresada = "Admin123"

if calve_ingresada != clave:
    intentos_fallidos += 1
    print(f"Intentos fallidos: {intentos_fallidos}")