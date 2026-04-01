#1. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
#. Tiene máximo 3 intentos para ingresar el PIN usando un while.
#3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
#4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
#5. Pregunta cuánto dinero quiere retirar.
#6. Usa un if para verificar:
#- Si el monto es mayor al saldo: "Fondos insuficientes".
#- Si el monto es igual a 0: "Monto inválido".
#- Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X".


saldo_del_usuario = 50000
intentos = 3
pin = 2202
pin_ingresado = 0
saldo_a_retirar = 0
while intentos > 0:
    print("bienvenido al cajero automatico pis seguro.")
    pin_ingresado = int(input("por favor ingrese su pin: "))
    print(f"tiene{intentos} intentos")

    if pin_ingresado != pin:
        print("pin incorrecto")
        intentos -= 1
    else:
        print("pin correcto")
        saldo_a_retirar = int(input("cuanto dinero quiere retirar: "))
        if saldo_a_retirar > saldo_del_usuario:
            print("saldo incuficiente")
        elif saldo_a_retirar == 0:
            print("monto invalido")
        else:
            saldo_del_usuario = saldo_del_usuario - saldo_a_retirar
            print(f"saldo exitoso su nuevo saldo es {saldo_del_usuario}")
else:
    print("no mas intentos, tajeta bloqueada")