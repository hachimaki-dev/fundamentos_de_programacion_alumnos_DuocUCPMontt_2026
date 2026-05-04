intentos_fallidos = 0
clave = "admin123"
clave_correcta = "secreto"
clave_ingresada = (input("ingrese la clave: "))
if clave_ingresada == clave_correcta:
    print("clave correcta")
else: 
    intentos_fallidos = intentos_fallidos + 1
    print(f"intentos_fallidos: {intentos_fallidos}")