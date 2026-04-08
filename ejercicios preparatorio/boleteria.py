precio_PV = 3000
precio_osorno = 7000
precio_frutillar = 5000

precio_final = 0
precio_boletos = 0
destino_1 = 1
destino_2 = 2
destino_3 = 3


cantidad_boletos = None
boleto_ida = 1
boleto_ida_vuelta = 2

print("BIENVENIDO A CRUZ AZUL")
print("====================")
print("ELIJA SU DESTINO:")
print(f"-     1. Puerto Varas ${precio_PV} ")
print(f"-     2. Osrono ${precio_osorno} ")
print(f"-     3. Frutillar ${precio_frutillar} ")

opcion_destino = int(input("POR FAVOR ELIJA LA OPCION DE SU DESTINO: "))

if opcion_destino == 1:
    print(f"SU DESTINO ES PUERTO VARAS.\nSELECCIONE EL TIPO DE VIAJE:\n -     1. Solo ida ${precio_PV}.\n -     2. Ida y vuelta ${precio_PV * 2}.")
    opcion_viaje = int(input("INGRESE LA OPCION DE SU VIAJE: "))
    if opcion_viaje == 1:
        print("CUANTOS ASIENTOS DESEA COMPRAR?")
        cantidad_boletos = int(input("INGRESE LA CANDTIDAD DE ASIENTOS A COMPRAR: "))
        if cantidad_boletos > 0:
            precio_boletos = precio_PV * cantidad_boletos
            if precio_boletos > 10000:
                precio_final = precio_boletos * 0.9
                precio_descuento = precio_boletos - precio_final
                print(f"SUBTOTAL: {precio_boletos}")
                print(f"DESCUENTO: {precio_descuento}")
                print(f"TOTAL: {precio_final}")
            elif cantidad_boletos == 0:
                print("volviendo al menu")
            else:
                precio_final = precio_boletos
                print(f"SUBTOTAL: {precio_final}")


'''while True:
    try:
        
    except ValueError:
        print("POR FAVOR INGRESE UNA OPCION VALIDA")'''