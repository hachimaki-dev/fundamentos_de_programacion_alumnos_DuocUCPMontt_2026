Intentos_fallidos = 0
clave_correcta = "secreto"

while True:
    clave = input("Escribe tu clave unica: ").lower()
    if clave == clave_correcta:
        print("Clave correcta!")
        break
    else:
        Intentos_fallidos = Intentos_fallidos + 1
        print(f"Clave incorrecta, intentos fallidos: {Intentos_fallidos}")
        break