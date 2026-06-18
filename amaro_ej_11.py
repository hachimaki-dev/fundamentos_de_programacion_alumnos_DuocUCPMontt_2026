intentos_fallidos = 0
clave = input("Ingrese la clave: ")
if clave == "secreto":
    print("Puedes entrar")
    print(f"Intentos fallidos: {intentos_fallidos}")
else:
    intentos_fallidos += 1
    print(f"Intentos fallidos: {intentos_fallidos}")