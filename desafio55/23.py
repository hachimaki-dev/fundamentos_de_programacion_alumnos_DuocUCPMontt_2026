intentos_fallidos = 0
insertar_clave = ""
clave = "a"
max_intentos = 3
while True:
    insertar_clave = input("Inserte su clave ")
    if intentos_fallidos < max_intentos:
        intentos_fallidos +=1
        print(f"Intentos fallidos: {intentos_fallidos}")
    else:
        print("Bloqueo Tarjeta")
        break
