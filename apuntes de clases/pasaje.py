viaje_total = 0
opcion_destino1 = "puerto varas"
opcion_destino2 = "osorno"
opcion_destino3 = " frutillar"
print("Bienvenido a la boleteria")

seguir_vendiendo = False

while True:
    if seguir_vendiendo:
        continuar = input("1. Seguir vendiendo 2. cancelar")
        if continuar == 2 :
            seguir_vendiendo == True
        else:
            seguir_vendiendo == False

    print("elija su destino")
    print("1.  Puerto Varas $3.000 ")
    print("2.  Osorno $5.000 ")
    print("3.  frutillar $7.000 ")

    precio_destino1 = 3000
    precio_destino2 = 5000
    precio_destino3 = 7000

    opcion_destino = int(input("Elija un destino \n = "))


    if opcion_destino == 1 :
        print(f"Has seleccionado Puerto varas {precio_destino1}. \n pasaje de ida y vuelta {precio_destino1 * 2}")
        viaje_total += precio_destino1


    else:
        opcion_destino == 2 
        print (F"seleccionaste Osorno {precio_destino2} \n pasaje de ida y vuelta {precio_destino2 * 2}")
    
        tipo_viaje = int(input("Desea la opcion 1 o la opcion 2 \n:"))

        if tipo_viaje == 1 :
            viaje_total = viaje_total + precio_destino1
            print(f"Elijio solo pasaje de ida {precio_destino1}")

        elif tipo_viaje == 2 :
            print(f"Elijio la opcion de ida y vuelta {viaje_total + precio_destino1 * 2}")

            viaje_total = int(input(f"El monto a pagar es de {viaje_total}"))
            input("Desea pagar (si/no")

            if viaje_total == "si":
                print("Sientese y pongase comodo, ahora comenzara el recorrido. ")

            elif viaje_total == "no":
                print("debe retirarse. rechazo la transaccion")
                







