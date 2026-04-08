precio_PV = 3000
precio_fruti = 5000
precio_osorno = 7000
dinero_recaudado = 0
salir_o_no = 0
pasajes_frutillar = 0
pasajes_puertovaras = 0
pasajes_osorno = 0
#bandera
continuar = False
while True:
    
    destino_seleccionado = 0
    ida_oVuelta = 0
    print("BIENVENIDO A LA BOLETERIA JUANETE")
    print("Por favor elija su destino")
    print(f"1. Puerto Varas    - ${precio_PV}")
    print(f"2. Frutillar       - ${precio_fruti}")
    print(f"3. Osorno          - ${precio_osorno}")
    destino_seleccionado = int(input("Ingrese su destino "))

    if destino_seleccionado == 1:
        print("Ha seleccionado PV")
        print(f"""Tiene las siguientes opciones:
            1. Ida y vuelta  -${(precio_PV*2)}
            2. Solo ida      -${precio_PV} """)
        ida_oVuelta = int(input(""))
        if ida_oVuelta == 1:
            dinero_recaudado = dinero_recaudado + (precio_PV * 2)
            print(f"Ha seleccionado Ida y vuelta. Valor: {(precio_PV * 2)} pesos")
        elif ida_oVuelta == 2:
            print(f"Ha seleccionado Solo ida. Valor: {precio_PV}")
            dinero_recaudado = dinero_recaudado + precio_PV
        else:
            print("Por favor ingrese una opción válida")
    elif destino_seleccionado == 2:
        print("Ha seleccionado Frutillar")
        print(f"""Tiene las siguientes opciones:
            1. Ida y vuelta  -${(precio_fruti*2)}
            2. Solo ida      -${precio_fruti} """)
        ida_oVuelta = int(input(""))
        if ida_oVuelta == 1:
            dinero_recaudado = dinero_recaudado + (precio_fruti * 2)
            print(f"Ha seleccionado Ida y vuelta. Valor: {(precio_fruti * 2)} pesos")
        elif ida_oVuelta == 2:
            print(f"Ha seleccionado Solo ida. Valor: {precio_fruti}")
            dinero_recaudado = dinero_recaudado + precio_fruti
        else:
            print("Por favor ingrese una opción válida")
    elif destino_seleccionado == 3:
        print("Ha seleccionado Osorno")
        print(f"""Tiene las siguientes opciones:
            1. Ida y vuelta  -${(precio_osorno*2)}
            2. Solo ida      -${precio_osorno} """)
        ida_oVuelta = int(input(""))
        if ida_oVuelta == 1:
            dinero_recaudado = dinero_recaudado + (precio_osorno * 2)
            print(f"Ha seleccionado Ida y vuelta. Valor: {(precio_osorno * 2)} pesos")
        elif ida_oVuelta == 2:
            print(f"Ha seleccionado Solo ida. Valor: {precio_osorno}")
            dinero_recaudado = dinero_recaudado + precio_osorno
        else:
            print("Por favor ingrese una opción válida")
    else: 
        print("Por favor ingrese una opción válida")
    print("Desea seguir vendiendo pasajes?")
    print("1. SI                     2. NO")
    salir_o_no = int(input("¿Si o no? "))
    if salir_o_no == 1:
        print(".........")
    elif salir_o_no == 2:
        break
    else:
        print("Por favor ingrese una opción válida")

print(f"Recaudación del día ${dinero_recaudado}")