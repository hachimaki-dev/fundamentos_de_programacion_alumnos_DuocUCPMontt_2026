intentos_fallidos = 0
clabe = "Admin123"
clave = "secreto"
if clave == clabe:
    print("entraste")
else:
    intentos_fallidos += 1
    print(f"Intentos fallidos: {intentos_fallidos}")