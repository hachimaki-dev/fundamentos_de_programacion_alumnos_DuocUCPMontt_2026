# Simular un cajero con validación de seguridad.

"""
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

import sys

saldo_del_usuario = 42000
pin_del_usuario = 1337
intentos = 0
bloqueo_de_seguridad = True

print("Bienvenido, porfavor ingrese su PIN de tarjeta para continuar!")
while bloqueo_de_seguridad == True:
    pin_ingresado = int(input())
    if pin_ingresado == pin_del_usuario:
        break
    if pin_ingresado != pin_del_usuario:
        if intentos < 3:
            print("PIN invalido, intente denuevo")
            intentos += 1
        elif intentos == 3:
            continue
    if intentos >= 3:
        print("Tarjeta bloqueado por seguridad")
        sys.exit()

print("Verificacion exitosa, cuanto dinero desea retirar?")
dinero_por_retirar = int(input())
print(f"Saldo actual: ${saldo_del_usuario}")
if dinero_por_retirar == 0:
    print("Monto Invalido")
if dinero_por_retirar > saldo_del_usuario:
    print("Fondos insuficientes")
else:
    saldo_del_usuario -= dinero_por_retirar
    print(f"Retiro exitoso! su nuevo saldo es: ${saldo_del_usuario}")