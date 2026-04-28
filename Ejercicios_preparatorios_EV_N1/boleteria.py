total_venta = 0

precio_frutillar = 5000
precio_osorno = 7000
precio_puerto_varas = 3000

bandera = False
print("*****BIENVENIDO A CRUZ DEL SUR*****")

while True:
    if bandera:
        continuar_programa =  int(input("Desea ingresar otro cliente? 1. Sí 2.No"))

        if continuar_programa == 2:
            break
    
    bandera = True
    print("===Por favor indique su destino===")

    print("1. Frutillar $5000")
    print("2. Puerto Varas $3000")
    print("3. Osorno $7000")

    destino_elegido = int(input("Adonde desea ir")) 

    if destino_elegido == 1:
        print("Ahh entonces vas a frutillar")
        print(f"1. Ida {precio_frutillar} ")
        print(f"2. Ida y vuelta {precio_frutillar * 2}")

        tipo_viaje = int(input("Ingrese su opción")) 

        if tipo_viaje == 1:
            total_venta = total_venta + precio_frutillar

            print(f"Se a comprado un pasaje de ida hacia frutillar por un total de {precio_frutillar} y llevamos un total de {total_venta} en caja")
        else:
            total_venta = total_venta + (precio_frutillar * 2)
            print(f"Se a comprado  pasaje de ida y vuelta hacia frutillar por un total de {precio_frutillar * 2} y llevamos un total de {total_venta} en caja")

    elif destino_elegido == 2:
        print("Ahh entonces vas a Puerto Varas")
        print(f"1. Ida {precio_puerto_varas} ")
        print(f"2. Ida y vuelta {precio_puerto_varas * 2}")

        tipo_viaje = int(input("Ingrese su opción")) 

        if tipo_viaje == 1:
            total_venta = total_venta + precio_puerto_varas

            print(f"Se a comprado un pasaje de ida hacia Puerto Varas por un total de {precio_puerto_varas} y llevamos un total de {total_venta} en caja")
        else:
            total_venta = total_venta + (precio_puerto_varas * 2)
            print(f"Se a comprado  pasaje de ida y vuelta hacia Puerto Varas por un total de {precio_puerto_varas * 2} y llevamos un total de {total_venta} en caja")

    elif destino_elegido == 3:
        print("Ahh entonces vas a Osorno")
        print(f"1. Ida {precio_osorno} ")
        print(f"2. Ida y vuelta {precio_osorno * 2}")

        tipo_viaje = int(input("Ingrese su opción")) 

        if tipo_viaje == 1:
            total_venta = total_venta + precio_osorno

            print(f"Se a comprado un pasaje de ida hacia Osorno por un total de {precio_osorno} y llevamos un total de {total_venta} en caja")
        else:
            total_venta = total_venta + (precio_osorno * 2)
            print(f"Se a comprado  pasaje de ida y vuelta hacia Osorno por un total de {precio_osorno * 2} y llevamos un total de {total_venta} en caja")

    else:
        print("Opción invalida")
