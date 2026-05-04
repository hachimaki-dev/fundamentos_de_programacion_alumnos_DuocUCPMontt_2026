intentos_fallidos = 0

clave_usuario = "secreto"
clave_elegida = "Admin123"

if clave_usuario == clave_elegida :
    print("Entraste")

else:
    intentos_fallidos = intentos_fallidos + 1
    print(f"intentos fallidos: {intentos_fallidos}")

