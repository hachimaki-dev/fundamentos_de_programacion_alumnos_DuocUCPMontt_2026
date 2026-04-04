#1. El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
#2. Tiene máximo 3 intentos para ingresar el PIN usando un while.
#3. Si falla 3 veces, el programa termina de inmediato y muestra "Tarjeta bloqueada por seguridad".
#4. Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
#5. Pregunta cuánto dinero quiere retirar.
#6. Usa un if para verificar:
#- Si el monto es mayor al saldo: "Fondos insuficientes".
#- Si el monto es igual a 0: "Monto inválido".
#- Si es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X"

pin = "1152"
intentos = 0
intentos_max = 3
acceso_concedido = False
saldo = 460000

while intentos < intentos_max:
    pin_ingresado = input("Ingresa tu PIN: ")
    if pin_ingresado == pin:
        print ("Acceso concedido")
        acceso_concedido = True
        break
    else:
        intentos = intentos + 1
        intentos_restantes = intentos_max - intentos
        print (f"Intenta de nuevo. Te quedan {intentos_restantes} intentos")
if intentos == intentos_max:
    print("Tarjeta bloqueada por seguridad")

retiro = False
if acceso_concedido:
    while True:
        dinero_por_retirar = int(input("¿Cuánto deseas retirar?"))
        if dinero_por_retirar > saldo:
            print ("Fondos insuficientes")
        elif dinero_por_retirar == 0:
            print("Monto inválido")
        else:
            saldo = saldo - dinero_por_retirar
            print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
            retiro = True
            break
#ya voy entendiendo creo (:
