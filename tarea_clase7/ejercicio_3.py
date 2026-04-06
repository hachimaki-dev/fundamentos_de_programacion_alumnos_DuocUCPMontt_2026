saldo = 50000
print("*"*50)
print("Bienvenido a BancoEstado!")
print("*"*50)

while True:
    try:
        menu = int(input("Que desea realizar?\n1) Ver saldo\n2) Girar dinero\n3) Inversión\n4) Salir\n: "))
        if menu == 1:
            print(f"Tu saldo es de {saldo}")
        elif menu == 2:
            retirar = int(input("Cuanto dinero desea retirar?"))
    except ValueError:
        print("Ingresa una wea valida")