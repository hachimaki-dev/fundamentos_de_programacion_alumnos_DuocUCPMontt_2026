PIN = 7777
intentos_fallidos = 0

print("Bienvenido al cajero, si quieres retirar dinero debes de ingresar tu clave secreta.")

while True:
    try:
        clave = int(input("Ingresa la clave secreta de 4 digitos: "))
        if clave != PIN:
            intentos_fallidos += 1
            print(f"Clave incorrecta, llevas {intentos_fallidos} intentos.")
            if intentos_fallidos == 3:
                print("Demasiados fallos, se bloqueara la tarjeta por seguridad.")
                break
        elif clave == PIN:
            print("Clave correcta, puedes usar el servicio de cajero automatico.")
            break
        else:
            print("Ingresa una opción valida.")
    except ValueError:
        print("Ingresa solo números enteros")

    