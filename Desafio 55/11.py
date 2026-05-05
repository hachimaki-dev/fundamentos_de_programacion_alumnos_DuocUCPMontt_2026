intentos_fallidos=0

clave_escrita="Admin123"

clave_correcta="secreto"

if clave_escrita==clave_correcta:
    print("Clave correcta")
else:
    intentos_fallidos+=1
    print(f"Intentos fallidos:{intentos_fallidos}")

