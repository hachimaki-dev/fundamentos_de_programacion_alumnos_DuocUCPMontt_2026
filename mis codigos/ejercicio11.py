intentos_fallidos = 0
clave_ingresada = "admin123"
clave_correcta = "secreto"

if clave_ingresada == clave_correcta:
    print("--Ingresaste--")

else:

  intentos_fallidos = intentos_fallidos + 1

print(f"intentos fallidos \n: {intentos_fallidos}")