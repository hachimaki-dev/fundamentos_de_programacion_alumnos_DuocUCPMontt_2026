saldo = 50000
intentos_restantes = 3
pin = 2009
bandera = True
bandera2 = True

print("Bienvenido a el cajero de Python. Para ingresar, dicte su Pin")
print("Recuerde que el pin es de 4 DIGITOS")

while bandera and intentos_restantes > 0:
    pin_ingresado = int(input("Ingrese Pin"))

    if pin_ingresado != pin:
        intentos_restantes = intentos_restantes - 1
        print("El pin ingresado es incorrecto")
    else:
        bandera = False
        print("Acceso concedido")
if intentos_restantes == 0:
    print("La tarjeta ha sido bloqueada por seguridad")

print(f"Su saldo actual es de ${saldo} CLP.")
print("")
print("")

while bandera2:
    saldo_retiro = int(input("¿Cuanto dinero necesita retirar?"))
    if saldo_retiro <= 0:
        print("El monto seleccionado es insuficiente. Por favor ingrese un nuevo monto")
    elif saldo_retiro > saldo:
            print("Saldo insuficiente, por favor ingrese nuevamente su dinero a Retirar")
    else:
        saldo = saldo - saldo_retiro
        bandera2 = False
        print(f"El dinero ha sido retirado con éxito. El saldo actual es de ${saldo}CLP")