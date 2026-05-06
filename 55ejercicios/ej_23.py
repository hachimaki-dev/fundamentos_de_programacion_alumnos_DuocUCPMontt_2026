# Ejercicio 23: Bloqueo de Seguridad (Cajero)

print("===============================")
print("Bienvenido al Cajero Automático")
print("===============================")

clave_correcta = "2344"
intentos_fallidos = 0

while True:

    clave = input("Ingrese su clave de 4 dígitos: ")

    if clave == clave_correcta:
        print("Acceso a la cuenta")
        break

    else:
        intentos_fallidos = intentos_fallidos + 1
        print("Clave incorrecta")

    if intentos_fallidos == 3:
        print("Bloqueo de Tarjeta")
        break