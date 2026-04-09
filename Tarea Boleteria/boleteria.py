total_caja = 0
Puerto_Varas = 3000
Frutillar = 5000
Osorno = 7000
bandera = False

print("Bienvenido a la boleteria de Cruz del Sur")

while True:  
    
    if continuar_vendiendo:
        desea_continuar = int(input("1. Continuar 2. Salir")
        if desea_continuar == 1:
            bandera = True
        else:
            break
    else:
        print("Elija una opcion correcta")
    bandera = True
    
    print("Por favor, ingrese su destino")
    print(f"1. Puerto Varas - Valor ${Puerto_Varas}")
    print(f"2. Frutillar - Valor ${Frutillar}")
    print(f"3. Osorno - Valor ${Osorno}")

    opcion_elejida =  int(input("Seleccione su destino"))

    if opcion_elejida == 1:
        print(f"Ha seleccionado Puerto Varas, la ciudad de las rosas. El costo de ida es {Puerto_Varas} y de ida y vuelta es de {Puerto_Varas * 2}")
        print("1. Ida")
        print("2. Ida y vuelta")
        tipo_viaje = int(input("Ingrese su tipo de viaje"))
        if tipo_viaje == 1:
            print(f"Su destino es Puerto Varas, su total es de {Puerto_Varas}")
            total_caja = total_caja + Puerto_Varas
        elif tipo_viaje == 2:
            total_caja = total_caja + (Puerto_Varas * 2)
            print(f"Su destino es Puerto Varas, su total es de {Puerto_Varas * 2}")
            
    elif opcion_elejida == 2:
        print(f"Ha seleccionado Frutillar, la ciudad de las frutillas. El costo de ida es {Frutillar} y de ida y vuelta es de {Frutillar * 2}")
        print("1. Ida")
        print("2. Ida y vuelta")
        tipo_viaje = int(input("Ingrese su tipo de viaje"))
        if tipo_viaje == 1:
            print(f"Su destino es Frutillar, su total es de {Frutillar}")
            total_caja = total_caja + Frutillar
        elif tipo_viaje == 2:
            total_caja = total_caja + (Frutillar * 2)
            print(f"Su destino es Frutillar, su total es de {Frutillar * 2}")

    elif opcion_elejida == 3:
        print(f"Ha seleccionado Osorno, la ciudad de las vaquitas. El costo de ida es {Osorno} y de ida y vuelta es de {Osorno * 2}")
        print("1. Ida")
        print("2. Ida y vuelta")
        tipo_viaje = int(input("Ingrese su tipo de viaje"))
        if tipo_viaje == 1:
            print(f"Su destino es Osorno, su total es de {Osorno}")
            total_caja = total_caja + Osorno
        elif tipo_viaje == 2:
            total_caja = total_caja + (Osorno * 2)
            print(f"Su destino es Osorno, su total es de {Osorno * 2}")