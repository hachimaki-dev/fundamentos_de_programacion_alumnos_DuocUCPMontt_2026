intentos_fallidos = 0

clave = "secreto"


ingreso_clave = input("Ingrese la clave: ")

if ingreso_clave == clave:
    print("¡Clave correcta! Acceso concedido.")
else:
    intentos_fallidos += 1
    print(f"Intento fallido: {intentos_fallidos}")