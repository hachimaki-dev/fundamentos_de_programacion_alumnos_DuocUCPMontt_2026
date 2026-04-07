#Simulación de Banco Virtual (Ciclos IF Anidados)

saldo = 50000

opcion = int(input("ingrese una opcion 1. ver saldo 2. girar dinero 3. inversion 4. salir "))
while opcion != 4:
    if opcion == 1:
        print (saldo)
    elif opcion == 2:
        giro = int (input("cuanto desea girar"))
        if giro <= saldo:
            if giro & 5000 == 0:
                saldo - giro
            else:
                print("monto no aceptado")
        else:
            print("saldo insuficiente")
                
            
            
        
        