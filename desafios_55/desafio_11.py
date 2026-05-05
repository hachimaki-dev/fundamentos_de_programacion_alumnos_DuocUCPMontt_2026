intento_fallidos = 0
clave = "Admin123"

if clave == "secreto":
    print("Ingresaste")

else:
    intento_fallidos += 1
    print(f"Intentos fallidos: {intento_fallidos}")