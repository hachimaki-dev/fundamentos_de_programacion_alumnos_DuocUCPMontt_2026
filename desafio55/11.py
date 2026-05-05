intentos_fallidos = 0
clave = "secreto"
user_input = "Admin123"
if user_input == clave:
    print("Entraste")
else:
    intentos_fallidos+= 1
    print(f"Intentos fallidos : {intentos_fallidos}.")