contraseña_ingresada = "nose"
contador_intentos_fallidos = 0
contraseña = "messi"
while contador_intentos_fallidos < 3:
    if contraseña_ingresada != contraseña:
        print("--contra incorrecta--")
        contador_intentos_fallidos += 1
        if contador_intentos_fallidos == 3:
            print("--Bloqueo de tarjeta--")
            exit 
    else:
        print("--contraseña correcta--")
        break
    



