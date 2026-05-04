total_caja = 0
precio_destino_1 = 3200
precio_destino_2 = 5000
precio_destino_3 = 7000
print("***Bienvenido/a a la boleteria de Cruz del Sur****")

#FLGS /BANDERAS
continuar_vendiendo = False
while True:

    if continuar_vendiendo:
        desea_continuar = int(input("1. Continuar 2. Salir"))
        if desea_continuar == 1:
            continuar_vendiendo = True
        else:
            break
    else:
        print("elija una opcion correcta")
    
    continuar_vendiendo = True



    print("Por favor ingrese su destino")
    print(f"1. Puerto Varas    - ${precio_destino_1}")
    print(f"2. Frutillar       - ${precio_destino_2}")
    print(f"3. Osorno          - ${precio_destino_3}")

    destino_seleccionado =  int(input("Seleccione su destino") )

    if destino_seleccionado == 1 :
        print(f"Ha seleccionado Puerto Varas la ciudad de las rosas, el costo de ida es {precio_destino_1} y el costo de ida y vuelta es {precio_destino_1 * 2}")
        print("1. Ida")
        print("2. Ida y vuelta")

        tipo_viaje = int(input("Ingrese su tipo de viaje"))

        if tipo_viaje == 1:
            print(f"Su destino es Puerto Varas, el total de su compra es {precio_destino_1}")
            total_caja = total_caja + precio_destino_1
        elif tipo_viaje == 2 :
            print(f"Su destino es Puerto Varas, el total de su compra es {precio_destino_1 * 2}")
            total_caja = total_caja + (precio_destino_1 * 2)
        else:
            print("Ingrese una opcion valida!")


    elif destino_seleccionado == 2 :
        print(f"Ha seleccionado Frutillar la ciudad de las frutillas, el costo de ida es {precio_destino_2} y el costo de ida y vuelta es {precio_destino_2 * 2}")
        print("1. Ida")
        print("2. Ida y vuelta")

        tipo_viaje = int(input("Ingrese su tipo de viaje"))

        if tipo_viaje == 1:
            print(f"Su destino es Frutillar, el total de su compra es {precio_destino_2}")
            total_caja = total_caja + precio_destino_2
        elif tipo_viaje == 2 :
            print(f"Su destino es Frutillar, el total de su compra es {precio_destino_2 * 2}")
            total_caja = total_caja + (precio_destino_2 * 2)
        else:
            print("Ingrese una opcion valida!")

    elif destino_seleccionado == 3 :
        print(f"Ha seleccionado Osorno la ciudad de las vaquitas, el costo de ida es {precio_destino_3} y el costo de ida y vuelta es {precio_destino_3 * 2}")
        print("1. Ida")
        print("2. Ida y vuelta")

        tipo_viaje = int(input("Ingrese su tipo de viaje"))

        if tipo_viaje == 1:
            print(f"Su destino es Osorno, el total de su compra es {precio_destino_3}")
            total_caja = total_caja + precio_destino_3
        elif tipo_viaje == 2 :
            print(f"Su destino es Osorno, el total de su compra es {precio_destino_3 * 2}")
            total_caja = total_caja + (precio_destino_3 * 2)
        else:
            print("Ingrese una opcion valida!")