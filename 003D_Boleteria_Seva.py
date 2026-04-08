Dinero_recaudado = 0
pasaje_puerto_varas = 3000
pasaje_Osorno = 7000
pasaje_frutillar =5000

print("---Bienvenido a la boleteria mi mami---")

print("Por favor elija su destino")
print(f"1. Puerto Varas     ${pasaje_puerto_varas}")
print(f"2. Osorno           ${pasaje_Osorno}")
print(f"3. Frutillar        ${pasaje_frutillar}")
while True:
    Destino_seleccionado = int(input("Ingrese su destino"))

    if Destino_seleccionado == 1 :
        print(f"Has seleccionado Puerto Varas, la ciudad de las rosas, la tarifa es de  {pasaje_puerto_varas})")
        print(f"1. Solo ida  {pasaje_puerto_varas},  2. de ida y de vuelta {pasaje_puerto_varas *2}")
        tipo_viaje = int(input("Seleccione su tipo de viaje \n"))
        if tipo_viaje == 1: 
            print(f"Has seleccionado pasaje de ida por un valor de  {pasaje_puerto_varas}")
            Dinero_recaudado += pasaje_puerto_varas
        elif tipo_viaje == 2:
            print(f"Has selecciondo pasaje de ida y vuelta por un valor de  {pasaje_puerto_varas *2}")
            Dinero_recaudado = Dinero_recaudado + (pasaje_puerto_varas *2)
        else:
            print("Por favor ingresa una opcion valida")
    

    if Destino_seleccionado == 2 :
        print(f"Has seleccionado Osorno, la ciudad de las vacas, la tarifa es de  {pasaje_Osorno})")
        print(f"1. Solo ida  {pasaje_Osorno},  2. de ida y de vuelta {pasaje_Osorno *2}")
        tipo_viaje = int(input("Seleccione su tipo de viaje \n"))
        if tipo_viaje == 1: 
            print(f"Has seleccionado pasaje de ida por un valor de  {pasaje_Osorno}")
            Dinero_recaudado += pasaje_Osorno
        elif tipo_viaje == 2:
            print(f"Has selecciondo pasaje de ida y vuelta por un valor de  {pasaje_Osorno *2}")
            Dinero_recaudado = Dinero_recaudado + (pasaje_Osorno*2)
        else:
            print("Por favor ingresa una opcion valida")

    if Destino_seleccionado == 3 :
     print(f"Has seleccionado Puerto Varas, la ciudad de las rosas, la tarifa es de  {pasaje_frutillar})")
     print(f"1. Solo ida  {pasaje_frutillar},  2. de ida y de vuelta {pasaje_frutillar *2}")
     tipo_viaje = int(input("Seleccione su tipo de viaje \n"))
     if tipo_viaje == 1: 
          print(f"Has seleccionado pasaje de ida por un valor de  {pasaje_frutillar}")
          Dinero_recaudado += pasaje_puerto_varas
     elif tipo_viaje == 2:
         print(f"Has selecciondo pasaje de ida y vuelta por un valor de  {pasaje_frutillar *2}")
         Dinero_recaudado = Dinero_recaudado + (pasaje_frutillar *2)
     else:
        print("Por favor ingresa una opcion valida")
    Seguir = input("¿Quiere seguir comprando boletos? Presione 1 para seguir comprando" "")
    if Seguir == "1": 
        print("")
    else:
        break
    