total_venta = 0

precio_frutillar = 5000
precio_osorno = 7000
precio_puerto_varas = 3000

print("****Bienvenido a la boleteria****")
print("==Por favor indique su destino==")

print("1. frutillar $5000") 
print("2. osorno $7000")
print("3. puerto varas $3000")

destino_elegido = int(input("adonde desea ir"))

if destino_elegido == 1:
     print(f"1.ida {precio_frutillar} ")
    
     print(f"2.ida y vuelta {precio_frutillar * 2} ")
    
     tipo_de_viaje = int(input("ingrese su opcion"))

if destino_elegido == 1:
    
    total_venta = total_venta + precio_frutillar
    
    print(f"se a comprado un pasaje a frutillar por un total de {precio_frutillar * 2} y llevamos un total de {total_venta} en caja")
    
else:
        
    total_venta = total_venta + {precio_frutillar * 2}
    print(f"se a comprado un pasaje a frutillar por un total de {precio_frutillar * 2} y llevamos un total de {total_venta} en caja")

    elif destino_elegido == 2:
        
    print(f"1.ida {precio_osorno}")
    print(f"2. ida y vuelta {precio_osorno * 2}")
    
    if destino_elegido == 2:
    total_venta = total_venta + precio_osorno
    print(f"se a comprado un pasaje a osorno por un total de {precio_osorno * 2} y llevamos un total de {total_venta} en caja")
else:
    
    total_venta = total_venta + {precio_osorno * 2}
    print(f"se a comprado un pasaje a osorno por un total de {precio_osorno * 2} y llevamos un total de {total_venta} en caja")
    
