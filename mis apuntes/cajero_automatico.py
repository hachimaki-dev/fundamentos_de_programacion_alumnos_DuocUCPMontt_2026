saldo= 50000
pin_correcto =1234
intentos =0
acceso = False  

while intentos <3:
    pin= int(input("ingrese clave:"))

    if pin == pin_correcto:
        acceso = True
        break
    else:
        print("pin incorrecto")
        intentos += 1

if not acceso:
    print("tarjeta bloqueada")
else:
    retiro = int(input(" ingrese monto a retirar"))

    if retiro > saldo:
        print("fondo insuficiente")

    elif retiro <= saldo: 
      saldo = saldo - retiro
      print("tu saldo actual es:",saldo)
      print("retiro exitoso")
    
