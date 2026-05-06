intentos_fallidos = 0
while True:
    input("Ingrese contraseña: ")
    intentos_fallidos = intentos_fallidos + 1
    if intentos_fallidos == 3:
        break
print(intentos_fallidos)