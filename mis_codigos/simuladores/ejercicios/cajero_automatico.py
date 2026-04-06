# El usuario tiene un saldo fijo (ej. $50.000) y un PIN secreto predefinido (ej. 1234).
saldo = 50000
pin_secreto = 1234
# Tiene máximo 3 intentos para ingresar el PIN usando un while
while pin_secreto != int(input("Ingrese su PIN: ")): # Si ingresa el PIN correcto, el ciclo de seguridad se corta, y pasamos al menú de retiro.
    print("PIN incorrecto. Intente nuevamente.")
    if pin_secreto != int(input("Ingrese su PIN: ")):
        print("PIN incorrecto. Intente nuevamente.")
        if pin_secreto != int(input("Ingrese su PIN: ")):
            print("PIN incorrecto. No tiene más intentos.")
            exit()
# Pregunta cuánto dinero quiere retirar.
monto_retiro = int(input("Ingrese el monto que desea retirar: "))
# Usa un if para verificar:
if monto_retiro > saldo:
    # Si el monto es mayor al saldo: "Fondos insuficientes".
    print("Fondos insuficientes.")
    # Si el monto es igual a 0: "Monto inválido".
elif monto_retiro == 0:
    print("Monto inválido.")
    # i es válido, resta el dinero, y muestra "Retiro exitoso. Su nuevo saldo es: $X"
else:    saldo -= monto_retiro
print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")