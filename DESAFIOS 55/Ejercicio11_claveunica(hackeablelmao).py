intentos_fallidos=0
clave="Admin123"
clavecorrecta = "secreto"
if clave==clavecorrecta:
    print("CORRECTO")
else:
    intentos_fallidos +=1
    print(f"Intentos fallidos: {intentos_fallidos}")