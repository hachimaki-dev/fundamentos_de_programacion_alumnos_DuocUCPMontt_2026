intentos = 0
contraseña = 1234
contraseña_ingresada = 1111
while True:
    if contraseña_ingresada != contraseña:
        intentos = intentos + 1
        if intentos == 3:
            print("bloqueo de tarjeta")
            break
    
