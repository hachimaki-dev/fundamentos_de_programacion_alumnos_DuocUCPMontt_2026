total_venta = 0
precio_frutillar = 5000
precio_puertovaras = 3000
precio_osorno = 7000
bandera = False

print("----BIENVENIDO A CRUZ DEL SUR")

while True:
    if bandera:
        continuar_programa = int(input("Desea ingresar otro cliente  1. Si  2.No"))
        
        if continuar_programa == 2:
            break
        
    bandera = True
    
    print("====Por favor indique su destino====")


    print("1. Frutillar $5000")
    print("2. Puerto Varas $3000")
    print("3. Osorno $7000")

    destino_elegido = int(input("¿Cual es su destino?"))

    if destino_elegido == 1:
        print(f"1. ida {precio_frutillar}")
        print(f"2. Ida y vuelta {precio_frutillar *2}")
        
        tipo_viaje = int(input("Ingrese su opción"))
        
        
        if tipo_viaje == 1:
            total_venta = total_venta + precio_frutillar
            print(f"Se ha comprado un pasaje de ida a frutillar por {precio_frutillar}")
            
        else:
            total_venta = total_venta + (precio_frutillar * 2)
            print(f"Se ha comprado un pasaje de ida y vuelta a frutillar por {precio_frutillar * 2} y llevamos un total de {total_venta} en caja")
            
    elif destino_elegido == 2:
        print(f"1. ida {precio_puertovaras}")
        print(f"2. Ida y vuelta {precio_puertovaras *2}")
        
        tipo_viaje = int(input("Ingrese su opción"))
        
        
        if tipo_viaje == 1:
            total_venta = total_venta + precio_puertovaras
            print(f"Se ha comprado un pasaje de ida a Puerto Varas por {precio_puertovaras}")
            
        else:
            total_venta = total_venta + (precio_puertovaras * 2)
            print(f"Se ha comprado un pasaje de ida y vuelta a Puerto Varas por {precio_puertovaras * 2} y llevamos un total de {total_venta} en caja")
            
            
    elif destino_elegido == 3:
        print(f"1. ida {precio_osorno}")
        print(f"2. Ida y vuelta {precio_osorno *2}")
        
        tipo_viaje = int(input("Ingrese su opción"))
        
        
        if tipo_viaje == 1:
            total_venta = total_venta + precio_osorno
            print(f"Se ha comprado un pasaje de ida a frutillar por {precio_osorno}")
            
        else:
            total_venta = total_venta + (precio_osorno * 2)
            print(f"Se ha comprado un pasaje de ida y vuelta a frutillar por {precio_osorno * 2} y llevamos un total de {total_venta} en caja")   
        