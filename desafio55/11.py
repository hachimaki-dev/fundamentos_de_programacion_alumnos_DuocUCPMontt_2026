intentos_fallidos= 0
clave_correcta= "secreto"
clave_ingresada= ""
while clave_ingresada != clave_correcta:
    clave_ingresada= input("Ingrese una clave: ").lower()

    if clave_ingresada != clave_correcta:
        intentos_fallidos += 1
        print(f"Te haz equivocado, tienes {intentos_fallidos} intentos fallidos")
    else:
        print(f"Felicidades, ingresaste la clave correcta en {intentos_fallidos} intentos")