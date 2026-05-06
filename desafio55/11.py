contador = 0

clave_correcta = "secreto"

clave = input("Ingrese su clave: ")

if clave == clave_correcta:
    print("Entrando...")
else:
    contador += 1
    print(f"Intentos fallidos: {contador}")