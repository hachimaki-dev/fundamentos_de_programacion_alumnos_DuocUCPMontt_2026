Saldo = 100000
Pin = 3028
Errores = 0
print("bienvenido")
Respuesta = int(input("ingrese su contraseña"))
while Respuesta != Pin :
    Errores = Errores + 1
    print("contraseña incorrecta, vuelve a intentarlo")
    Respuesta = int(input("ingrese su contraseña"))
    if Errores == 2 :
        print("demasiados errores bloqueo por seguidad")
        break
    break
print("contraseña correcta")
Retiro = int(input("cuanto dinero quiere retirar"))
while Retiro > Saldo :
    print("saldo insuficiente")
    if Retiro < Saldo :
        print("retiro exitoso")
        Saldo = Saldo - Retiro
        print(f"tu nuevo saldo es {Saldo}")
    elif Retiro == 0 :
        print("monto invalido")
    Retiro = int(input("cuanto dinero quiere retirar"))    