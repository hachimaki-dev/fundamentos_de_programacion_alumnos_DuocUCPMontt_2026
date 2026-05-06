intentos_fallidos = 0
clave = "Admin123"

if clave == "secreto":
    print("Entrastes")
else:
    intentos_fallidos += 1
    print("Intentos fallidos:" , intentos_fallidos)
