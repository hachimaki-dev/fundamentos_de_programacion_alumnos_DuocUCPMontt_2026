intentos_fallidos=0
clave_ingresada="Admin123"
clave_secreta="secreto"
if clave_ingresada==clave_secreta:
    print("Entraste")
else:
    intentos_fallidos+=1
    print(f"Intentos fallidos: {intentos_fallidos}")