clave = "Admin123"
intentos_fallidos = 0

if clave != "secreto":
    intentos_fallidos += 1
    print(f"Intentos fallidos: {intentos_fallidos}")
else:
    print("Acceso permitido!")