saldo = 50000
intentos_restantes = 3
pin = 2009
bandera = True
bandera2 = True
import time

print("Bienvenido a el cajero de Python. Para ingresar, dicte su Pin")
print("Recuerde que el pin es de 4 DIGITOS")
time.sleep (5)
while bandera and intentos_restantes > 0:
    pin_ingresado = int(input("Ingrese Pin"))

    if pin_ingresado != pin:
        intentos_restantes = intentos_restantes - 1
        print("El pin ingresado es incorrecto")
    elif pin_ingresado == pin:
        bandera = False
        print("...")
        time.sleep (2)
        print("Acceso concedido")
    else:
        print("Ingrese caracteres validos (Ejemplo, 0123, 1230, etc")
if intentos_restantes == 0:
    print("La tarjeta ha sido bloqueada por seguridad")
    import sys
    sys.exit()
    
time.sleep (3)
print(f"Su saldo actual es de ${saldo} CLP.")
print("")
print("")

while bandera2:
    saldo_retiro = int(input("¿Cuanto dinero necesita retirar?"))
    if saldo_retiro <= 0:
        print("El monto seleccionado es insuficiente. Por favor ingrese un nuevo monto")
    elif saldo_retiro > saldo:
            print("Saldo insuficiente, por favor ingrese nuevamente su dinero a retirar")
    else:
        saldo = saldo - saldo_retiro
        bandera2 = False
        print("...")
        time.sleep (2)
        print(f"El dinero ha sido retirado con éxito. El saldo actual es de ${saldo}CLP")