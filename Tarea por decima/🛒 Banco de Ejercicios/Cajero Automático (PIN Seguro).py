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


saldo = 50000
pin_user = "1234" 
intentos = 0
intentos_totales = 3
acceso_concedido = False

print("***** BIENVENIDOS A BANCO ESTADO EL PATITO FELIZ *****")

while intentos < intentos_totales:
    pin_ingresado = input("Ingrese su PIN: ")

    if pin_ingresado == pin_user:
        print("Acceso permitido")
        acceso_concedido = True
        break
    else:
        print("Acceso denegado")
        intentos += 1
        if intentos == intentos_totales:
            print("Tarjeta bloqueada por seguridad")

if acceso_concedido == True:
        monto = int(input("¿Cuanto saldo desea retirar?: "))
        if monto <= 0:
            print("Monto invalido")
        elif monto > saldo:
            print("Saldo Insuficientes")
        else:
            monto = saldo - monto
            print(f"Retiro exitoso. Su nuevo saldo es {monto}")

print("Fin del programa")