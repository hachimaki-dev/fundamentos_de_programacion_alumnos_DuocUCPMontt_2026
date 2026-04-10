total_caja= 0
pasaje_pv= 3000
pasaje_fr= 5000
pasaje_os= 7000

print("=====BIENVENIDO=====")
while True:
    
    print("LOS DESTINOS A ELEGIR SON: Puerto Varas, Frutillar y Osorno")
    print(f"1.>>Puerto Varas: {pasaje_pv}")
    print(f"2.>>Frutillar: {pasaje_fr}")
    print(f"3.>>Osorno: {pasaje_os}")

    destino= input("\nELIGE TU DESTINO (1/2/3): ")

    if destino == "1":
        print("DESTINO SELECCIONADO: Puerto Varas")
        tipo_viaje= input("QUE TIPO DE VIAJE ELIGE? (1: IDA/2: IDA Y VUELTA): ")
        if tipo_viaje == "1":
            print(f"TU TOTAL ES DE {pasaje_pv}")
            total_caja += pasaje_pv
            otro_pasaje= input("DESEA COMPRAR OTRO PASAJE? (1. SI/2. NO): ")
            if otro_pasaje == "1":
                continue
            elif otro_pasaje == "2":
                break
        elif tipo_viaje == "2":
            print(f"TU TOTAL ES DE {pasaje_pv * 2}")
            total_caja += pasaje_pv * 2
            otro_pasaje= input("DESEA COMPRAR OTRO PASAJE? (1. SI/2. NO): ")
            if otro_pasaje == "1":
                continue
            elif otro_pasaje == "2":
                break
        else:
            print("INGRESA UNA OPCION VALIDA")
            continue
    if destino == "2":
        print("DESTINO SELECCIONADO: Frutillar")
        tipo_viaje= input("QUE TIPO DE VIAJE ELIGE? (1: IDA/2: IDA Y VUELTA): ")
        if tipo_viaje == "1":
            print(f"TU TOTAL ES DE {pasaje_fr}")
            total_caja += pasaje_fr
            otro_pasaje= input("DESEA COMPRAR OTRO PASAJE? (1. SI/2. NO): ")
            if otro_pasaje == "1":
                continue
            elif otro_pasaje == "2":
                break
        elif tipo_viaje == "2":
            print(f"TU TOTAL ES DE {pasaje_fr * 2}")
            total_caja += pasaje_fr * 2
            otro_pasaje= input("DESEA COMPRAR OTRO PASAJE? (1. SI/2. NO): ")
            if otro_pasaje == "1":
                continue
            elif otro_pasaje == "2":
                break
            else:
                print("INGRESE UNA OPCION VALIDA")
        else:
            print("INGRESA UNA OPCION VALIDA")
            continue
    if destino == "3":
        print("DESTINO SELECCIONADO: Osorno")
        tipo_viaje= input("QUE TIPO DE VIAJE ELIGE? (1: IDA/2: IDA Y VUELTA): ")
        if tipo_viaje == "1":
            print(f"TU TOTAL ES DE {pasaje_os}")
            total_caja += pasaje_os
            otro_pasaje= input("DESEA COMPRAR OTRO PASAJE? (1. SI/2. NO): ")
            if otro_pasaje == "1":
                continue
            elif otro_pasaje == "2":
                break
        elif tipo_viaje == "2":
            print(f"TU TOTAL ES DE {pasaje_os * 2}")
            total_caja += pasaje_os * 2
            otro_pasaje= input("DESEA COMPRAR OTRO PASAJE? (1. SI/2. NO): ")
            if otro_pasaje == "1":
                continue
            elif otro_pasaje == "2":
                break
        else:
            print("INGRESA UNA OPCION VALIDA")
            continue

print("GRACIAS POR COMPRAR!")
print(f"GANANCIAS TOTALES SON: {total_caja}")