intentos_fallidos = 0
clave = "admin123"
if clave == "secreto":
    print("entraste")
else:
    intentos_fallidos = intentos_fallidos + 1
    print("Intentos fallidos: ", intentos_fallidos)

