"""
Cajero Automático (PIN Seguro)
Objetivo: Simular un cajero con validación de seguridad.

1. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
2. Tiene máximo 3 intentos para ingresar el PIN usando un while.
3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
5. Pregunta cuánto dinero quiere retirar.
6. Usa un if para verificar:
- Si el monto es mayor al saldo: "Fondos insuficientes".
- Si el monto es igual a 0: "Monto inválido".
- Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X".
"""
Saldo = 100.000
Intentos_PIN = 3

while Intentos_PIN > 0:
    codigo = int(input("Inserta tu PIN "))
    if codigo != 2167:
        Intentos_PIN = Intentos_PIN - 1
        print(f"PIN incorrecto, intentos restantes {Intentos_PIN}")
    else:
        print("PIN correcto")
        break
if Intentos_PIN == 0:
    print("Tarjeta bloqueada por seguridad")
else:
    while True:
        Dinero = int(input("Cuanto dinero quieres retirar? (-1 = Salir)"))
        if Dinero > Saldo:
            print("Fondos insuficientes")
        elif Dinero <= 0 and Dinero != -1:
            print("Monto inválido")
        elif Dinero > 0 and Dinero <= Saldo:
            Saldo = Saldo - Dinero
            print(f"Retiro exitoso. Su nuevo saldo es: ${Saldo}")
        elif Dinero == -1:
            break
