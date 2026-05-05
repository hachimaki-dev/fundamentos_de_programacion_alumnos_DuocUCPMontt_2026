intentos_fallidos = 0
clave_correcta = "secreto"

intento = input("ingrese la clave; ")

if intento == clave_correcta: 
    print("La contraseña es correcta: ")

else: 
    intento != clave_correcta

    intentos_fallidos = intentos_fallidos + 1 

    print(f"intentos fallidos: {intentos_fallidos}")
