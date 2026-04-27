saldo = 50000
PINsecreto = 1972
intentos = 0

print("==== BIENVENIDO AL CAJERO ====")

while intentos < 3:
    Pin_ingresado = int(input("Ingrese su PIN : "))
    if Pin_ingresado == PINsecreto:
        print("Haz ingresado al Menú.")         #SE COLOCA UN CICLO QUE REPITA HASTA 3 VECES PARA NOSOTROS PODER INGRESAR EL PIN
        break
    else:
        print("PIN INCORRECTO.")
        intentos += 1


if intentos == 3:
    print("Tarjeta bloqueada por seguridad.")   #SI EL NUMERO DE INTENTOS ES IGUAL A 3 TERMINARA EL PROGRAMA COLOCANDO UN PRINT

if intentos < 3:
    monto = int(input("Ingrese el monto que desea retirar : "))
    if monto > saldo:
        print("Fondo insuficiente.")
    elif monto == 0:
        print("Monto invalido.")
    else:
        saldo -= monto
        print(f"Retiro Exitoso, su saldo actual es de ${saldo} pesos.")