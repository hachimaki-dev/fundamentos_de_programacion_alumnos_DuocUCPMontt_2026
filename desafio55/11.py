intentos_fallidos = 0
clave_correcta = "secreto"
clave_incorrecta = "Admin123"

while True:
    clave = input("¿Cual es la clave?")
    if clave == clave_correcta :
        print("Entraste")
        break

    else:
        clave == clave_incorrecta
        intentos_fallidos = intentos_fallidos + 1
        print(f"Clave incorrecta, Intentos {intentos_fallidos}")
