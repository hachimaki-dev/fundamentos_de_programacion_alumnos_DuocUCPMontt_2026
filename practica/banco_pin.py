#. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
#2. Tiene máximo 3 intentos para ingresar el PIN usando un while.
#3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
#4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
#5. Pregunta cuánto dinero quiere retirar.
#6. Usa un if para verificar:
#- Si el monto es mayor al saldo: "Fondos insuficientes".
#- Si el monto es igual a 0: "Monto inválido".
#- Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X".

pin = 9837
saldo = 50000
intento = 3
pin_ingresado = 0
monto = 0
while intento > 0 :
    print("ingrese su clave")
    pin_ingresado = int(input())
    if pin_ingresado == pin :
        print("acceso aprovado")
        monto = int(input("monto a sacar"))
        if monto > saldo :
            print("saldo insuficiente")
        elif monto == 0 :
            print("monto invalido")
        else:
            saldo = saldo - monto
            print(f"retiro exitoso, su saldo disponible es {saldo}")

    elif pin_ingresado != pin :
        intento = intento - 1
        print(f"clave incorrecta {intento} intentos disponibles")
else:
    print("cuenta bloqueada")

