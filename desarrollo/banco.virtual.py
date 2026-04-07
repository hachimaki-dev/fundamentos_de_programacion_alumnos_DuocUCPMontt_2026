import time
import sys

saldo_inicial = 500000

print ("/===========================/")
print ("/=======BANCO VIRTUAL=======/")
print ("/===========================/\n")

print ("Bienvenido a nuestro banco virtual.")
print ("Aquí podras hacer tus transacciones desde la comdidad de tu hogar.")
print ("En unos minutos le mostraremos el menú.\n")

print ("ESPERE PACIENTEMENTE...")
time.sleep(3)

print ("/===========================/")
print ("/==========MENÚ=============/")
print ("/===========================/\n")

print ("1. Ver saldo.")
print ("2. Girar dinero.")
print ("3. Inversión.")
print ("4. Salir.\n")

print (f"Le recordamos que cuenta con un saldo de ${saldo_inicial}.")
print ("En la sección de abajo, podra ingresar su acción.")

while True :
    eleccion_de_usuario = int(input("¿Qué desea realizar? : "))
    
    if eleccion_de_usuario == 1 :
        print ()
        print ("PROCESANDO...\n")

        print (f"Usted cuenta con un saldo de ${saldo_inicial}.")

        print("¿Desea hacer otra consulta? Confirme con (SI/NO).")
        opcion = str(input("Confirmar su acción : ")).lower()
        print()
        if opcion == "si":
            print ("Bien, cuentenos que más desea saber.")

        elif opcion == "no":
            print ("Que tenga un buen día.")
            print ("Gracias por visitarnos.")
            break

    elif eleccion_de_usuario == 2 :
        print ()
        print ("PROCESANDO...\n")
        time.sleep(5)

        print ("¡Diganos cuanto monto desea girar?")
        monto_a_girar = int(input("Monto a girar : "))
        print ()

        if monto_a_girar > 0:
            print ("¿Usted esta seguro de girar dinero? Confirme (SI/NO).")
            confirmacion = str(input("Confirmar respuesta : ")).lower()
            print (f"Bien, recuerde que cuenta con un saldo de {saldo_inicial}.\n")
            if confirmacion == "si" and saldo_inicial > monto_a_girar:
                saldo_inicial = saldo_inicial - monto_a_girar
                print ()
                print ("Se ha retirado su dinero de manera correcta.")
                print (f"Ahora cuenta con un saldo {saldo_inicial}.")
                print ("Que tenga un buen día.\n")

            elif confirmacion == "si" and saldo_inicial < monto_a_girar:
                print ("Saldo insuficiente.")
                print ("Pruebe con otro monto.")
                print ()

            
            elif confirmacion == "no":
                print ("¿Desea hacer otra acción?")
                reafirmación = str(input("confirme con (SI/NO) : ")).lower()
                print()
                if reafirmación == "si":
                    print ("Bien, continue.")
                    print ()
                elif reafirmación == "no":
                    print ("Que tenga un buen día.")
                    break

            else:
                print ("Ingrese solo (SI o NO).")

    elif eleccion_de_usuario == 3:
        print ("Ha seleecionado inversión.")
        print ("Para poder invertir, te vamos a pedir una cantidad para agregarlo al monto.")
        print ("Ingrese su monto en la sección de abajo.\n")
        inversion_de_usuario = str("Ingrese el monto que desea invertir :")
        print ()

        if inversion_de_usuario >0:
            print(f"¿Usted esta seguro que desea invertir la cantidad ${inversion_de_usuario}?")
            print ("Confirme en la sección de abajo con (SI o NO).\n")
            reafirmación_2 = str(input("Ingrese su confirmación : ")).lower()
            print ()

            if reafirmación_2 == "si" and saldo_inicial > inversion_de_usuario:
                print ("Se ha agregado su inversión con exito.")
                saldo_inicial = saldo_inicial * inversion_de_usuario
                print (f"Usted ahora cuenta con {saldo_inicial}.")

            elif reafirmación_2 == "si" and saldo_inicial < inversion_de_usuario:
                print ("Saldo insuficiente.")

            elif reafirmación_2 == "no":
                print()
                print("¿Desea hacer otra acción?")
                mega_afimrancion = str(input("Confirme su acción : ")).lower()
                print()

                if mega_afimrancion == "Si":
                    print ("BIEN.")
                    
                elif mega_afimrancion == "no":
                    break
    elif eleccion_de_usuario == 4:
        break
                
print ("Cajero apagado")




        

            



