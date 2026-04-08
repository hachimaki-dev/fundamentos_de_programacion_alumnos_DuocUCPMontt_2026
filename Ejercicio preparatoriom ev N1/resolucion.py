total_venta = 0

precio_frutillar = 5000
precio_osorno = 7000
precio_puerto_varas = 3000

print("bienvenido a la boleteria")

print("porfavor indique su destino")

print("1. frutillar $5000") 

print("2. puerto varas $3000") 

print("3. osorno $7000")

destino_elegido = int(input("adonde desea ir"))

if destino_elegido == 1:
    print(f"1.1 ida {precio_frutillar}")
    print(f"2. Ida y vuelta {precio_frutillar * 2}")
    tipo_viaje = int(input("ingrese su opcion:"))
    
    if tipo_viaje == 1 :
        total_venta = total_venta + precio_frutillar
        print(f" aaaasu compra de pasaje a frutillar se a realizado con exito con total de {precio_frutillar} con un total en caja de {total_venta + precio_frutillar}")
       
    else: 
        total_venta = total_venta + (precio_frutillar *2)
        print(f" su compra de pasaje a frutillar se a realizado con exito con total de {precio_frutillar * 2} jeje con un total en caja de {total_venta + (precio_frutillar * 2)}")

elif destino_elegido == 2:
    print(f"1. ida {precio_osorno}")
    print(f"2. Ida y vuelta {precio_osorno * 2}")
    input("ingrese su opcion:")
    if tipo_viaje == 2 :
        total_venta = total_venta + precio_frutillar
        print(f" su compra de pasaje a frutillar se a realizado con exito con total de {precio_osorno} con un total en caja de {total_venta}")
       
    else: 
        total_venta = total_venta + {precio_osorno *2}
        print(f" su compra de pasaje a frutillar se a realizado con exito con total de {precio_osorno} con un total en caja de {total_venta * 2}")

    