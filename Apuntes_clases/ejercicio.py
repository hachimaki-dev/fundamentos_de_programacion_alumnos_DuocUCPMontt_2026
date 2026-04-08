#boleteria
total_recaudado = 0

nombre_destino1 = "Puerto Varas"
nombre_destino2 = "Frutillar"
nombre_destino3 = "Osorno"

Precio_destino1 = "$3000"
Precio_destino2 = "$5000"
Precio_destino3 = "$7000"

print("bienvenido/a a Cruz del sur")

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
    print("Elija su destino")
    print("   -    1.Puerto Varas  $3.000")
    print("   -    2.Frutillar    $5.000")
    print("   -    3.Osorno    $7.000")

    opcion_Destino = int(input("Por favor ingrese su destino \n"))

    if opcion_Destino == 1:

        print(f"Has seleccionado Puerto Varas, la ciudad de las rosas el costo es 1. Pasaje de ida{Precio_destino1} \n 2. Pasaje de ida y vuelta {Precio_destino1 * 2} ")

        tipo_viaje = int(input("Va de ida? o ida y vuelta?"))

        if tipo_viaje == 1:
            print(f"Ha elegido de ida, el costo es {Precio_destino1}")
            total_recaudado = total_recaudado + Precio_destino1
        elif tipo_viaje == 2:
            print(f"Ha elegido de ida y vuelta, el costo es {Precio_destino1 * 2}")
            total_recaudado = total_recaudado + (Precio_destino1 * 2)
        else:
            print("¡¡Por favor elija entre 1 o 2!!")

    elif opcion_Destino == 2:

        print(f"Has seleccionado Frutillar, la ciudad de las frutillas el costo es 1. Pasaje de ida{Precio_destino2} \n 2. Pasaje de ida y vuelta {Precio_destino2 * 2} ")

        tipo_viaje = int(input("Va de ida? o ida y vuelta?"))

        if tipo_viaje == 1:
            print(f"Ha elegido de ida, el costo es {Precio_destino2}")
            total_recaudado = total_recaudado + Precio_destino2
        elif tipo_viaje == 2:
            print(f"Ha elegido de ida y vuelta, el costo es {Precio_destino2 * 2}")
            total_recaudado = total_recaudado + (Precio_destino2 * 2)
        else:
            print("¡¡Por favor elija entre 1 o 2!!")

    elif opcion_Destino == 3:

        print(f"Has seleccionado Osorno, la ciudad de las rosas el costo es 1. Pasaje de ida{Precio_destino3} \n 2. Pasaje de ida y vuelta {Precio_destino3 * 2} ")

        tipo_viaje = int(input("Va de ida? o ida y vuelta?"))

        if tipo_viaje == 1:
            print(f"Ha elegido de ida, el costo es {Precio_destino3}")
            total_recaudado = total_recaudado + Precio_destino3
        elif tipo_viaje == 2:
            print(f"Ha elegido de ida y vuelta, el costo es {Precio_destino3 * 2}")
            total_recaudado = total_recaudado + (Precio_destino3  * 2)
        else:
            print("¡¡Por favor elija entre 1 o 2!!")