totalrecaudado = 0
venta = True

print("Bienvenida Terminal de Buses")

while venta == True:
    precio = 0
    valoracobrar = 0
    destino = ""
    while True:
        print(f"Por favor elija su destino: \n 1. Puerto Varas - $3.000 \n 2. Frutillar - $5.000 \n 3. Osorno - $7000")
        opciondestino = int(input("\n Indique su opcion: \n"))
        if opciondestino == 1:
            destino="Puerto Varas"
            precio=3000
            break

        elif opciondestino == 2:
            destino="Frutillar"
            precio=5000
            break
        elif opciondestino == 3:
            destino="Osorno"
            precio=7000
            break
        else:
            print ("Opcion invalida")    

    print(f"Destino elegido {destino}")

    print(f"\n 1) Solo Ida \n 2) Ida y Vuelta ")
    opcionidayvuelta = int(input("Indique opción"))
    while True:
        if opcionidayvuelta == 1:
            break
        elif opcionidayvuelta == 2:
            precio = 2 * precio
            break
        else:
            print ("Opción invalida")
    
    print ("\n¿Cuantos pasajes desea comprar?")
    while True:
        cantidadpasajes = int(input("\nIngrese cantidad: "))
        if cantidadpasajes > 0:
            precio = precio * cantidadpasajes
            break
        else:
            print("Opción Invalida")

    print (f"Valor total pasajes: ${precio}")

    if precio > 10000:
        valoracobrar = precio - (precio*0.1)
        print ("DESCUENTO DEL 10% Aplicado")
    else:
        valoracobrar = precio
    print(f"\n Usted debe pagar ${valoracobrar}")

    totalrecaudado += valoracobrar
    print ("¿Atender otro cliente? y/n")
    opcionreseteo= input("")
    while True:
        if opcionreseteo == "y":
            venta = True
            break
        elif opcionreseteo == "n":
            venta = False
            break
        else:
            print("Opcion invalida")   

print (f"Total recaudado: {totalrecaudado}")


