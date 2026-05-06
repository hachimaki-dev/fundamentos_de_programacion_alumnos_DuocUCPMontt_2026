intentos_fallidos= 0
clave_correcta= 1234

while intentos_fallidos < 3:
    clave_ingresada= int(input("Ingrese una clave: "))
    if clave_ingresada == clave_correcta:
        print("Haz entrado!")
        break
    else:
        print("Clave incorrecta, intenta de nuevo")
        intentos_fallidos += 1

print("Haz superado el limite de intentos, Bloqueando tarjeta")