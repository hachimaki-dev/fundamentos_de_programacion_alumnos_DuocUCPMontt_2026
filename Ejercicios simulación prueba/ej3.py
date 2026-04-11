#Variables cajero automático
saldo = 50000
operacion = 0

#Bienvenida al usuario
print("---Bienvido/a a Banco Estado---\n")
#operaciones del cajero autmático
print("1) Ver Saldo")
print("2) Girar Dinero")
print("3) Inversión")
print("4) Salir")

while operacion != 4:
    operacion = int(input("¿Qué operación desea realizar?\n(Presiona 4 para salir)\n"))
# Aquí el usuario ve su saldo actual
    if operacion == 4:
        print("Cajero apagado")
        break
    elif operacion == 1:
        print(f"Tu saldo es: ${saldo}")
#retiro de dinero
    elif operacion == 2:
        retiro = int(input("¿Cuánto desea retirar?\n$"))
        if retiro <= saldo and retiro % 5000 == 0:
            saldo -= retiro
            print(f"Has retirado: ${retiro}\nTu saldo actual es: ${saldo}")
        elif retiro > saldo:
            print("Saldo insuficiente")
        else:
            print("Monto no aceptado")
# inversión
    elif operacion == 3:
        inversion = int(input("¿cuánto deseas invertir?\n $"))
        if inversion <= saldo:
            saldo = (saldo - inversion) + (inversion * 2)
            print (f"Has invertido: ${inversion}\n Tu saldo actual es: ${saldo}")
    else:
        print("Opción inválida")
