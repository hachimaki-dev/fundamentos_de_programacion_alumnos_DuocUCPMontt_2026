saldo = 50000
opcion_elegida = 0
saldo_a_retirar = 0
invercion = 0
saldo_para_invertir = 0
print("bienvenido al banco valdi")
while True:
    print("tienes todas estas opciones")
    print("1. ver saldo")
    print("2. girar dinero")
    print("3. invertir")
    print("4. salir")
    opcion_elegida = int(input("elige una opcion "))

    if opcion_elegida == 1:     
        print(f"tu saldo es de {saldo}")

    elif opcion_elegida == 2:
        print("solo puedes retirar una cantidad multiplo de 5")
        saldo_a_retirar = int(input("cuando dinero vas a sacar "))
        if saldo_a_retirar <= saldo and saldo_a_retirar %5 == 0:
            saldo -= saldo_a_retirar
            print(f"retiro con exito tu saldo actual es de {saldo}")
        else :  
            print("error en tiens que sacar un monto que sea menor a tu saldo y tiene que ser multiplo de 5") 
    
    elif opcion_elegida == 3:
        print("elige cuanto dinero de tu saldo vas a duplicar")
       
        saldo_para_invertir = int(input("monto a invertir: "))
        
        if saldo_para_invertir <= saldo:
            saldo -= saldo_para_invertir # Quitamos lo que vas a invertir del saldo
            inversion = saldo_para_invertir * 2 # Duplicamos solo lo invertido
            saldo += inversion # Lo sumamos de vuelta al saldo total
            print(f"tu inversión se ha multiplicado a {inversion}")
            print(f"ahora en total tienes {saldo}")
        else:
            print("No tienes saldo suficiente.")

    elif opcion_elegida == 4:
        break
    
        



