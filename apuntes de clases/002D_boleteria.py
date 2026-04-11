total_caja = 0
precio_destino1 = 3200
precio_destino2 = 5000
precio_destino3 = 7000

print("**** Bienvenidos a la boleteria de cruz del sur ****")

print("Por favor ingrese su destino ")
print(f"1. puerto varas : {precio_destino1}")
print(f"2. Frutillar : {precio_destino2}")
print(f"3: osorno : {precio_destino3}")

destino_seleccionado = int(input("seleccione su destino:  "))

if destino_seleccionado == 1:
    print(f"has seleccionado puerto varas , el costo de ida es {precio_destino1} y ida y vuelta {precio_destino1 * 2}")
    
    print("1 . ida")
    print("2. ida y vuelta")
    tipo_viaje = int(input("ingrese su tipo de  viaje"))

    if tipo_viaje == 1:
        print(f"su destino es puerto varas , el total de su compra es {precio_destino1} ")
        total_caja += precio_destino1
    elif tipo_viaje == 2:
        total_caja += precio_destino1 * 2
    
