intentos_fallidos = 0 

clave = "secreto"

if clave == "Admin123":
    print("entraste")

else:
    intentos_fallidos = intentos_fallidos + 1
    print(f"intentos fallidos: {intentos_fallidos}")


