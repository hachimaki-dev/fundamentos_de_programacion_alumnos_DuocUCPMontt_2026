intentos_fallidos = 0
contraseña = "1234"

while intentos_fallidos < 3:
    ingreso = input("Ingrese la contraseña: ")
    if ingreso == contraseña:
        print("contraseña es correcta")
        break
    else:
        print("bloqueo de tarjeta")
        intentos_fallidos += 1