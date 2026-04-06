print("bienvenido")
saldo = 50000
while True :
    print("elija una opcion")
    print("1-- ver saldo")
    print("2-- girar dinero")
    print("3-- inversion")
    print("4-- salir")
    respuesta = int(input("elija su opcion"))
    if respuesta == 4 :
        print("cajero apagado")
        print("salir")
        break
    elif respuesta == 1 :
        print(f"su saldo actual es {saldo}")
    elif respuesta == 2 :
    
        print("ingreso giro")
        print("debe ser multiplo de 5000")
        giro = int(input("cuanto vas a girar"))
        if giro >= saldo :
            print("saldo insuficiente")
        elif giro < saldo :
            print("ha elegido giro")
            if giro%5000 == 0 :
                saldo = saldo - giro
                print(f"su nuevo saldo es {saldo}")
            else :
                print("monto no valido")

                
    




    elif respuesta == 3 :
        print("inversion")    
        invert = int(input("ingrese cantidad a invertir"))
        if invert >= saldo :
            print("saldo insuficiente")
        elif invert < saldo :
            print(f"su inversion fue {invert}")
            saldo = saldo + invert*2
            nose = invert*2
            print(f"su nuevo saldo es {saldo}")
            print(f"su inversion genero {nose}")

