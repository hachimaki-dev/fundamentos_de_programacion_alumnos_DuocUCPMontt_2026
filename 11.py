intentos_fallidos = 0
clave_correcta = "secreto"

clave_unica = input("ingrese la clave unica: ")

if clave_unica == clave_correcta:
    print("has entrado")

else:
    print(f"intentos fallidos: {intentos_fallidos + 1}")
