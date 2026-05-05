intentos_fallidos = 0
contraseña = "secreto"

usuario = input("ingrese su contraseña: ")
if usuario != contraseña :
    intentos_fallidos = +1
    print(f"intentos fallidos: {intentos_fallidos}")
else :
    print("acceso concedido")