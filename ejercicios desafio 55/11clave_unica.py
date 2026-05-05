intentos_fallidos = 0
clave = "secreto"
intento = input("escribe la clave: ")
if intento != "secreto":
    intentos_fallidos = intentos_fallidos + 1 
    print(f"intentos fallidos: {intentos_fallidos}")
else:
    print("has ingresado exitosamente")