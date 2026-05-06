intentos_fallidos = 0
clave = "Admin123"

if clave == "Secreto":
    print("Entraste")
else:
    intentos_fallidos += 1
    print(f"Intentos fallidos: {intentos_fallidos}")