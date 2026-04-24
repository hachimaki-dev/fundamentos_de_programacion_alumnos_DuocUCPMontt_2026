dinero_recaudado = 0

precio_destino_Puerto_varas = 3000
Precio_destino_Frutillar = 5000
Precio_destino_Osorno = 7000 

print("BIENVENIDO A LA BOLETERIA JuanBuses")

Continuar = False


while True:

    if Continuar:
        int(input("1. Continuar 2. Salir")
        Continuar = True
    else:
        break
Continuar = True
print("Por favor elija su destino")
print("1. Puerto Varas   - ${precio_destino_Puerto_varas}")
print("2. Frutillar      - $5000")
print("3. Osorno         - $7000")

Destino_seleccionado = int(input("ingrese su destino"))

if Destino_seleccionado ==1 :
    print("a seleccionado Puerto varas y la tarifa es de ${precio_destino_Puerto_varas}")
    print("1. solo ida ${precio_destino_Puerto_varas}")
    print("2. de ida y vuelta ${precio_destino_Puerto_varas * 2}")
    tipo_viaje = int(input("seleccione su tipo de viaje \n"))
    if tipo_viaje ==1:
        print("Ha seleccionado pasaje de ida y su valor es ${precio_destino_Puerto_varas}")
        dinero_recaudado = dinero_recaudado +  {precio_destino_Puerto_varas}

    elif tipo_viaje == 2:
        print("ha seleccionado pasaje de ida y vuelta por un valor de ${precio_destino_Puerto_varas}2")
        dinero_recaudado = dinero_recaudado + ({precio_destino_Puerto_varas * 2})

    else:
        print("Porfavor ingrese una opcion valida")

print("Por favor elija su destino")
print("1. Puerto Varas   - $3000")
print("2. Frutillar      - ${Precio_destino_Frutillar}")
print("3. Osorno         - $7000")

Destino_seleccionado = int(input("ingrese su destino"))

if Destino_seleccionado ==1 :
    print("a seleccionado Frutillar y la tarifa es de ${Precio_destino_Frutillar}")
    print("1. solo ida ${Precio_destino_Frutillar}")
    print("2. de ida y vuelta ${Precio_destino_Frutillar}")
    tipo_viaje = int(input("seleccione su tipo de viaje /n"))
    if tipo_viaje ==1:
        print("Ha seleccionado pasaje de ida y su valor es ${Precio_destino_Frutillar}")
        dinero_recaudado = dinero_recaudado + {Precio_destino_Frutillar}

    elif tipo_viaje == 2:
        print("ha seleccionado pasaje de ida y vuelta por un valor de ${Precio_destino_Frutillar}")
        dinero_recaudado = dinero_recaudado + ({Precio_destino_Frutillar * 2})

    else:
        print("Porfavor ingrese una opcion valida")

print("Por favor elija su destino")
print("1. Puerto Varas   - $3000")
print("2. Frutillar      - $5000")
print("3. Osorno         - ${Precio_destino_Osorno}")

Destino_seleccionado = int(input("ingrese su destino"))

if Destino_seleccionado ==1 :
    print("a seleccionado Osorno y la tarifa es de ${Precio_destino_Osorno}")
    print("1. solo ida ${Precio_destino_Osorno}")
    print("2. de ida y vuelta ${Precio_destino_Osorno}")
    tipo_viaje = int(input("seleccione su tipo de viaje /n"))
    if tipo_viaje ==1:
        print("Ha seleccionado pasaje de ida y su valor es ${Precio_destino_Osorno}")
        dinero_recaudado = dinero_recaudado +  {Precio_destino_Osorno}

    elif tipo_viaje == 2:
        print("ha seleccionado pasaje de ida y vuelta por un valor de ${Precio_destino_Osorno}")
        dinero_recaudado = dinero_recaudado +  (Precio_destino_Osorno * 2)

    else:
        print("Porfavor ingrese una opcion valida")


        