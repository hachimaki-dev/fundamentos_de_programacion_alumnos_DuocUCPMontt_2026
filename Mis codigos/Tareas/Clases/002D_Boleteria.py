puertovaras = 3000
frutillar = 5000
osorno = 7000

print("Bienvenido a la Boleteria de Cruz del Sur")
continuar_vendiendo = False
while True:

    if continuar_vendiendo:
        desea_continuar = int(input("1. Continuar 2. Salir"))
        if desea_continuar == 1:
            continuar_vendiendo = True
        else:
            break
    else:
        print("Elija una opcion correcta")

    continuar_vendiendo = True
    
    print("Por favor ingrese su destino")
    print(f"1. Puerto Varas - ${puertovaras}")
    print(f"2. Frutillar - ${frutillar}")
    print(f"3. Osorno - ${osorno}")

    total_Caja = 0
    lugar_destino = int(input("Seleccione su destino"))


    if lugar_destino == 1:
        total_Caja = total_Caja + puertovaras
    elif lugar_destino == 2:
        total_Caja = total_Caja + frutillar
    elif lugar_destino == 3:
        total_Caja = total_Caja + osorno
    else:
        print("Opcion no vàlida")

    tipo_de_viaje = int(input("Escoja el tipo de viaje que desea realizar"))

    if tipo_de_viaje == 1:
        print(f"Ha seleccionado Puerto Varas, el total de su compra es ${puertovaras}")
        total_Caja = total_Caja + puertovaras
    elif tipo_de_viaje == 2:
        print(f"Ha seleccionado Puerto Varas, el total de su compra es ${puertovaras * 2}")
        total_Caja = total_Caja + (puertovaras * 2)

    

