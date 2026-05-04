total_recaudado = 0

nombre_destino_1 = "Osorno"
nombre_destino_2 = "Frutillar"
nombre_destino_3 = "Puerto Varas"

precio_destino_1 = 3000
precio_destino_2 = 5000
precio_destino_3 = 7000



print("***Bienvenido/a a Cruz del Sur***")

#bandera = False

seguir_vendiendo = False

while True:

    if seguir_vendiendo:
        continuar = int(input("1. Seguir vendiendo 2. Salir"))
        if continuar == 2:
            seguir_vendiendo = True
            break
        else:
            seguir_vendiendo = False

    seguir_vendiendo = True
    print("    -    Elija su destino")
    print("    -        1.Puerto Varas  $3.000")
    print("    -        2.Frutillar     $5.000")
    print("    -        3.Osorno        $7.000")

    opcion_destino =  int(input("Por favor ingrese su destino \n"))


    if opcion_destino == 1 :

        print(f"Ha seleccionado Puerto Varas, la ciudad de la rosas el costo es: \n 1. Pasaje de ida {precio_destino_1} \n 2. Pasaje de ida y vuelta {precio_destino_1 * 2}")

        tipo_viaje = int(input("Va de ida? o de ida y vuelta?"))

        if tipo_viaje == 1 :
            print(f"Ha elegido de ida, el costo es {precio_destino_1}")
            total_recaudado = total_recaudado +   precio_destino_1
        elif tipo_viaje == 2 :
            print(f"Ha elegido de ida y vuelta, el costo es {precio_destino_1 * 2}")
            total_recaudado = total_recaudado +   ( precio_destino_1 * 2 )
        else:
            print("¡¡¡¡¡¡¡¡¡¡Por favor elija entre 1 o 2!!!!!!!!!!!!")

    elif opcion_destino == 2 :

        print(f"Ha seleccionado Frutillar, la ciudad de la frutillas el costo es: \n 1. Pasaje de ida {precio_destino_2} \n 2. Pasaje de ida y vuelta {precio_destino_2 * 2}")

        tipo_viaje = int(input("Va de ida? o de ida y vuelta?"))

        if tipo_viaje == 1 :
            print(f"Ha elegido de ida, el costo es {precio_destino_2}")
            total_recaudado = total_recaudado +   precio_destino_2
        elif tipo_viaje == 2 :
            print(f"Ha elegido de ida y vuelta, el costo es {precio_destino_2 * 2}")
            total_recaudado = total_recaudado +   ( precio_destino_2 * 2 )
        else:
            print("¡¡¡¡¡¡¡¡¡¡Por favor elija entre 1 o 2!!!!!!!!!!!!")


    elif opcion_destino == 3 :

        print(f"Ha seleccionado Osorno, la ciudad de la vacas el costo es: \n 1. Pasaje de ida {precio_destino_3} \n 2. Pasaje de ida y vuelta {precio_destino_3 * 2}")

        tipo_viaje = int(input("Va de ida? o de ida y vuelta?"))

        if tipo_viaje == 1 :
            print(f"Ha elegido de ida, el costo es {precio_destino_3}")
            total_recaudado = total_recaudado +   precio_destino_3
        elif tipo_viaje == 2 :
            print(f"Ha elegido de ida y vuelta, el costo es {precio_destino_3 * 2}")
            total_recaudado = total_recaudado +   ( precio_destino_3 * 2 )
        else:
            print("¡¡¡¡¡¡¡¡¡¡Por favor elija entre 1 o 2!!!!!!!!!!!!")


