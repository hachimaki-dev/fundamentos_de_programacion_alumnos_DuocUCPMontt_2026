intentos_fallidos = 0
clave = 'Admin123'
clave_real = 'secreto'

input("ingresa la clave: ")

if clave_real != clave:
    intentos_fallidos = (intentos_fallidos + 1)
    print(f"Intentos fallidos: {intentos_fallidos}")
else:
    print("desbloqueado")