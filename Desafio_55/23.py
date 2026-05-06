intentos_fallidos = 0
clave = "Profe goat"

while True:
    intento = input("Clave:")
    if intentos_fallidos == 2:
        print("Tarjeta bloqueada")
        break
    if intento != clave:
        intentos_fallidos = intentos_fallidos + 1
        print(f"intento fallidos: {intentos_fallidos}")
