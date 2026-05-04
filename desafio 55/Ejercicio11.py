intenos_fallidos = 0
clave_secreta = "secreto"

print(f"Bienvenido a tu clave unica")
while True:
    clave_ingresada = input("Por favor ingrese su clave")
    if intenos_fallidos == 2:
        print("CUENTA BLOQUEADA")
        print("CERRANDO EL PROGRAMA")
        break
    elif clave_ingresada == clave_secreta:
        print("Contraseña CORRECTA")
        print("Cerrando Programa")
        break
    else:
        intenos_fallidos = intenos_fallidos + 1
        print(f"Llevas {intenos_fallidos} intento/s fallido/s, te restan {3 - intenos_fallidos}")