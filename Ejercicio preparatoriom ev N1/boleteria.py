total_ventas = 0

precio_frutillar = 5000
precio_osorno = 7000
precio_Puerto_varas = 3000


bandera = False
print("---Bienvenidos a cruz del sur---")

while True:
    if bandera:
        continuar_programa = int(input("Desea ingresar otro cliente? 1. Si  2. No"))
        
        if continuar_programa == 2:
            break
        
    bandera = True
    print("--- Porfavor indique su destino: ---")

    print("1. Frutillar $5000")
    print("2. Puerto Varas $3000")
    print("3. Osorno $7000")

    Destino_elegido = int(input("A donde desea ir"))

    if Destino_elegido == 1:
        print(f"1. Ida {precio_frutillar}")
        print(f"2. ida y vuelta {precio_frutillar * 2}")
        
        tipo_viaje = int(input("Ingrese su opcion"))
        if tipo_viaje == 1:
            total_ventas = total_ventas + precio_frutillar
            print(f"se ah comprado un pasaje de ida hacia frutillar por un total de {precio_frutillar} y llevamos un total de {total_ventas} en caja")
            
        else:
            total_ventas = total_ventas + (precio_frutillar * 2)
            print(f"se ah comprado un pasaje de ida hacia frutillar por un total de {precio_frutillar * 2} y llevamos un total de {total_ventas} en caja")
        
        
            total_ventas += precio_frutillar 
            
    elif Destino_elegido == 2:
        print(f"1. Ida {precio_Puerto_varas}")
        print(f"2. ida y vuelta {precio_Puerto_varas * 2}")
        
        tipo_viaje = int(input("Ingrese su opcion"))
        if tipo_viaje == 1:
            total_ventas = total_ventas + precio_Puerto_varas
            print(f"se ah comprado un pasaje de ida hacia frutillar por un total de {precio_Puerto_varas} y llevamos un total de {total_ventas} en caja")
            
        else:
            total_ventas = total_ventas + (precio_Puerto_varas * 2)
            print(f"se ah comprado un pasaje de ida hacia frutillar por un total de {precio_Puerto_varas * 2} y llevamos un total de {total_ventas} en caja")
        
        
            total_ventas += precio_Puerto_varas 
            
    elif Destino_elegido == 3:
        print(f"1. Ida {precio_osorno}")
        print(f"2. ida y vuelta {precio_osorno * 2}")
        
        tipo_viaje = int(input("Ingrese su opcion"))
        if tipo_viaje == 1:
            total_ventas = total_ventas + precio_osorno
            print(f"se ah comprado un pasaje de ida hacia frutillar por un total de {precio_osorno} y llevamos un total de {total_ventas} en caja")
            
        else:
            total_ventas = total_ventas + (precio_osorno * 2)
            print(f"se ah comprado un pasaje de ida hacia frutillar por un total de {precio_osorno * 2} y llevamos un total de {total_ventas} en caja")
        
        
            total_ventas += precio_osorno
    
