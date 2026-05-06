intentos = 0
contraseña = 1337

while True: # Este codigo espera un int!
    clave = int(input("Ingrese su clave []: "))
    if clave != contraseña:
        print("Clave incorrecta!")
    if clave == contraseña:
        print("Acceso permitido!")
        break
    elif intentos >= 2:
        print("Tarjeta bloqueada")
        break
    intentos += 1