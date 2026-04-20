from site import ENABLE_USER_SITE
codigosecreto = "1234"
saldo=5000
intentosrestantes = 3
print("Bienvenido al banco estado (aqui de colina 1)")
print("1. Retirar dinero")
print("2. Invertir en los fondoh de droga.. digo de pensiones")
print("3 . Salir")
opciones = int(input("Ingrese opcion"))
while intentosrestantes > 0 :
    if opciones == 1:
         if input("Por favor ingrese tu pin secreto") == codigosecreto:
          print("Acceso concedido!")
         retiro = int(input("Cuanto desea retirar? $"))
    if retiro <= saldo :
        saldo-= retiro
        print(f"Operacion exitosa usted acaba de retirar ${retiro} . nuevo saldo disponible es : ${saldo}")
        print("Gracias por usar el sistema!!")
        break

    elif opciones == 2:
        inversiones = int(input("Ingrese cuanto dinero quiere invertir :"))
        inversiones = inversiones + (saldo * 0.4)
        print(f"Su nuevo saldo con un tasa de retorno del 4% es de {inversiones}")
        print("Gracias por usar el sistema!!")
        break
    retiro = int(input("Cuanto desea retirar? $"))
    if retiro <= saldo :
        saldo-= retiro
        print(f"Operacion exitosa usted acaba de retirar ${retiro} . nuevo saldo disponible es : ${saldo}")
        print("Gracias por usar el sistema!!")
        break
    else:
        print("Fondos insuficientes")
        break
else:
    intentosrestantes = intentosrestantes - 1
    if intentosrestantes > 0 :
     print("PIN INCORRECTO!")
    else :
        print("Alarma : se bloqueara sistmea!!")