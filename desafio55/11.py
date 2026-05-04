intentos_fallidos = 0
password = "secreto"

password_ingresada = input("Contraseña: ")

if password_ingresada == password:
    print("Acceso concedido")
else:
    intentos_fallidos = intentos_fallidos + 1
    print(f"Intentos fallidos: {intentos_fallidos}")
