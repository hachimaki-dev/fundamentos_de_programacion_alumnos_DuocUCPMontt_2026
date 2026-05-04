intentos_fallidos = 0
clave = "Admin123"
while True:
    clave_ingresada = input("Ingresa clave: ")
    if clave_ingresada != clave:
        intentos_fallidos += 1
        print(f"Intentos fallidos {intentos_fallidos}")
    else:
        print("Clave correcta.")
        break