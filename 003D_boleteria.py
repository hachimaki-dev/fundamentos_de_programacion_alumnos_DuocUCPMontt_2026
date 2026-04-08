dinero_recaudado = 0

precio_destino_puerto_varas = 3000
precio_destino_frutillar = 5000
precio_destino_osorno = 7000
oferta = 10
subtotal = 0

# banderas
continuar = False

while True :

    if continuar:
        desea_continuar = int(input("1. continuar 2. salir"))
        if desea_continuar == 1 :
            continue
        else:
            break
    continuar = True
    print("###bienvenida a la boleteria ###")
    print("elija su destino")
    print("1. puerto varas -$3300")
    print("2. frutillar    -$5000")
    print("3. osorno       -$7000")
    

    destino_seleccionado = int(input("engrese su destino"))
    if destino_seleccionado == 1 :
        print(f"ha seleccionado puerto varas la ciudad de las rosas y la tarifa es de {precio_destino_puerto_varas}")
        print(f"1. solo ida {precio_destino_puerto_varas}")
        print(f"2. ida y de vuelta {precio_destino_puerto_varas*2}")
        tipo_viaje = int(input("seleccione su tipo de viaje"))
        if tipo_viaje == 1 :
            print(f"ha seleccionado pasaje de ida, su valor es {precio_destino_puerto_varas}")
            dinero_recaudado = dinero_recaudado + precio_destino_puerto_varas
        elif tipo_viaje == 2 :
            print(f"ha seleccionado pasaje de ida y vuelta por un valor de {precio_destino_puerto_varas}")
            dinero_recaudado = dinero_recaudado + (precio_destino_puerto_varas*2)
        else:
            print("por favor ingrese una opcion valida")



    elif destino_seleccionado == 2 :
        print(f"ha seleccionado frutillar {precio_destino_frutillar}")
        print(f"1. solo ida {precio_destino_frutillar}")
        print(f"2. ida y de vuelta {precio_destino_frutillar*2}")
        tipo_viaje = int(input("seleccione su tipo de viaje"))
        if tipo_viaje == 1 :
            print(f"ha seleccionado pasaje de ida, su valor es {precio_destino_frutillar}")
            dinero_recaudado = dinero_recaudado + precio_destino_frutillar
        elif tipo_viaje == 2 :
            print(f"ha seleccionado pasaje de ida y vuelta por un valor de {precio_destino_frutillars}")
            dinero_recaudado = dinero_recaudado + (precio_destino_frutillar*2)
        else:
            print("por favor ingrese una opcion valida")



    elif destino_seleccionado == 3 :
        print(f"ha seleccionado osorno ciudad de las vacas {precio_destino_osorno}")
        print(f"1. solo ida {precio_destino_osorno}")
        print(f"2. ida y de vuelta {precio_destino_osorno*2}")
        tipo_viaje = int(input("seleccione su tipo* de viaje"))
        if tipo_viaje == 1 :
            print(f"ha seleccionado pasaje de ida, su valor es {precio_destino_osorno}")
            dinero_recaudado = dinero_recaudado + precio_destino_osorno
        elif tipo_viaje == 2 :
            print(f"ha seleccionado pasaje de ida y vuelta por un valor de {precio_destino_osorno}")
            dinero_recaudado = dinero_recaudado + (precio_destino_osorno*2)
        else:
            print("por favor ingrese una opcion valida")

            
   
