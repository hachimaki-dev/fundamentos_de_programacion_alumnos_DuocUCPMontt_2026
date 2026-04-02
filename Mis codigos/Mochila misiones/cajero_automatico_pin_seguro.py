# Cajero Automático (PIN Seguro)
# Objetivo: Simular un cajero con validación de seguridad.

# 1. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
# 2. Tiene máximo 3 intentos para ingresar el PIN usando un while.
# 3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
# 4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
# 5. Pregunta cuánto dinero quiere retirar.
# 6. Usa un if para verificar:
# - Si el monto es mayor al saldo: "Fondos insuficientes".
# - Si el monto es igual a 0: "Monto inválido".
# - Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X".

saldo = 10000
pin_secreto = 5678
intentos = 3
protege_cuenta = True

while protege_cuenta and intentos > 0:
    pin_ingresado = int(input("Ingrese su PIN secreto: "))
    intentos = intentos - 1
    if pin_ingresado != pin_secreto:
        print(f"PIN incorrecto, intentos restantes {intentos}")
    else:
        protege_cuenta = False
        retiro_dinero = int(input("Ingrese cantidad a retirar: "))
        if retiro_dinero == 0:
            print("Monto invalido")
            break
        if retiro_dinero > saldo:
            print("Fondos insuficientes")
        else:
            saldo = saldo - retiro_dinero
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")

if intentos == 0 and protege_cuenta:
    print("Tarjeta bloqueada por seguridad")