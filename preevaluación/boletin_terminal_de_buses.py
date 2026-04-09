import time
import sys

total_de_caja = 0
valor_de_puertovaras = 3000
valor_de_osorno = 7000
valor_de_frutillar = 5000

print ("/=======================/")
print ("/===Terminal de buses===/")
print ("/=======================/\n")

print ("Bienvendio a la boleteria de cruz del sur.")

print ("Vamos a cagar los tipo de boletos que tenemos.")
time.slee(3)

continuar_vendiendo = False

while True :

    if continuar_vendiendo:
        print ("1. Continuar.")
        print ("2. Salir.")

        deasea_continuar = int(input("Que desea hacer :"))
        if deasea_continuar == 1:
            continuar_vendiendo = True

        else:
            break

        
    print ("/===================/")
    print ("/=======MENÚ========/")
    print ("/===================/\n")

    print ("¿A que lugar desea ir?\n")

    print (f"1.    - Puerto Varas  ${valor_de_puertovaras}.")
    print (f"2.    - Osorno  ${valor_de_osorno}.")
    print (f"3.    - Frutillar $ {valor_de_frutillar}.")
    print ()

    print ("Ingrese a que destino desea ir, en la sección de abajo.\n")

    destino_elegido = int(input("Confirmar destino : "))
    print ()
    print ("Bien, ahora estamos procesando tu elección.\n")

    if destino_elegido == 1 :
        print (f"Usted quiere ir a Puerto Varas, el vieja de ida es {valor_de_puertovaras}.")
        print ("Pero, si escoge ida y vuelta, el cobro se aumenta a 6000.")
        print()

        print (f"1. IDA --> ${valor_de_puertovaras}.")
        print (f"2. IDA Y VUELTA --> $6000.\n")

        print ("¿Desea ir una vez o ir y volver?\n")


        metodo_de_ida = int(input("Confirme su destino : "))

        if metodo_de_ida == 1:
            print ("Bien, su boleta esta siendo procesada.")
            time.sleep(3)
            total_de_caja = total_de_caja + valor_de_puertovaras
            print ()
            print ("============")
            print ("===BOLETA===")
            print ("============\n")

            print (f"Coste de su boleta es ${valor_de_puertovaras}.")
            print ("Que tenga un buen viaje.")

        elif metodo_de_ida == 2:
            print ("Bien, su boleta esta siendo procesada.")
            time.sleep(3)
            total_de_caja = total_de_caja + (valor_de_puertovaras * 2)
            print ()
            print ("============")
            print ("===BOLETA===")
            print ("============\n")

            print (f"Coste de su boleta es ${total_de_caja}.")
            print ("Que tenga un buen viaje.")
            
        else:
            print ("Ingrese solo 1 o 2...")

    elif destino_elegido == 2 :
        print (f"Usted quiere ir a Osorno, el vieja de ida es {valor_de_osorno}.")
        print ("Pero, si escoge ida y vuelta, el cobro se aumenta a 14000.")
        print()

        print (f"1. IDA --> ${valor_de_osorno}.")
        print (f"2. IDA Y VUELTA --> $14000.\n")

        print ("¿Desea ir una vez o ir y volver?\n")


        metodo_de_ida = int(input("Confirme su destino : "))

        if metodo_de_ida == 1:
            print ("Bien, su boleta esta siendo procesada.")
            time.sleep(3)
            total_de_caja = total_de_caja + valor_de_osorno
            print ()
            print ("============")
            print ("===BOLETA===")
            print ("============\n")

            print (f"Coste de su boleta es ${valor_de_osorno}.")
            print ("Que tenga un buen viaje.\n")

        elif metodo_de_ida == 2:
            print ("Bien, su boleta esta siendo procesada.")
            time.sleep(3)
            total_de_caja = total_de_caja + (valor_de_osorno * 2)
            print ()
            print ("============")
            print ("===BOLETA===")
            print ("============\n")

            print (f"Coste de su boleta es ${total_de_caja}.")
            print ("Que tenga un buen viaje.")
            
        else:
            print ("Ingrese solo 1 o 2...")

        
    if destino_elegido == 3:
        print (f"Usted quiere ir a Frutillar, el vieja de ida es {valor_de_frutillar}.")
        print ("Pero, si escoge ida y vuelta, el cobro se aumenta a 10000.")
        print()

        print (f"1. IDA --> ${valor_de_frutillar}.")
        print (f"2. IDA Y VUELTA --> $10000.\n")

        print ("¿Desea ir una vez o ir y volver?\n")


        metodo_de_ida = int(input("Confirme su destino : "))

        if metodo_de_ida == 1:
            print ("Bien, su boleta esta siendo procesada.")
            time.sleep(3)
            total_de_caja = total_de_caja + valor_de_puertovaras
            print ()
            print ("============")
            print ("===BOLETA===")
            print ("============\n")

            print (f"Coste de su boleta es ${valor_de_puertovaras}.")
            print ("Que tenga un buen viaje.")

        elif metodo_de_ida == 2:
            print ("Bien, su boleta esta siendo procesada.")
            time.sleep(3)
            total_de_caja = total_de_caja + (valor_de_puertovaras * 2)
            print ()
            print ("============")
            print ("===BOLETA===")
            print ("============\n")

            print (f"Coste de su boleta es ${total_de_caja}.")
            print ("Que tenga un buen viaje.")
            
        else:
            print ("Ingrese solo 1 o 2...")
        



