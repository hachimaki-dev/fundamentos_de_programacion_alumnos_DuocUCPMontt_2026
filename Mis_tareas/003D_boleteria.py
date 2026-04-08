recaudado=0
puerto_varas=3000
osorno=7000
frutillar=5000
respuesta=""
#capacidad=0

print("Bienvenido/a a la boleteria Juan buses")
while True:
    print("====Elija su destino====")
    print(f"1-Puerto Varas     -${puerto_varas}")
    print(f"2-Osorno           -${osorno}")
    print(f"3-Frutillar        -${frutillar}")

    destino_usuario = int(input("Ingrese su destino: "))

    if destino_usuario ==1:
        print("Has elejido Puerto Varas")
        print(f"1- Solo ida      -${puerto_varas}")
        print(f"2- Ida y vuelta  -${puerto_varas*2}")
        tipo_de_viaje = int(input("seleccione su tipo de viaje: "))
        if tipo_de_viaje ==1:
            print(f"Seleccionado solo ida, su valor es de ${puerto_varas}")
            recaudado += puerto_varas
        elif tipo_de_viaje==2:
            print(f"Seleccionado ida y vuelta por un valor de ${puerto_varas *2}")
            recaudado+= puerto_varas*2
        else:
            print("Opcion no valida")
    elif destino_usuario==2:
        print("Has elejido Osorno")
        print(f"1- Solo ida      -${osorno}")
        print(f"2- Ida y vuelta  -${osorno*2}")
        tipo_de_viaje = int(input("seleccione su tipo de viaje: "))
        if tipo_de_viaje ==1:
            print(f"Seleccionado solo ida, su valor es de ${osorno}")
            recaudado += osorno
        elif tipo_de_viaje==2:
            print(f"Seleccionado ida y vuelta por un valor de ${osorno *2}")
            recaudado+= osorno*2
        else:
            print("Opcion no valida")
    elif destino_usuario==3:
        print("Has elejido Frutillar ")
        print(f"1- Solo ida      -${frutillar}")
        print(f"2- Ida y vuelta  -${frutillar*2}")
        tipo_de_viaje = int(input("seleccione su tipo de viaje: "))
        if tipo_de_viaje ==1:
            print(f"Seleccionado solo ida, su valor es de ${frutillar}")
            recaudado += frutillar
        elif tipo_de_viaje==2:
            print(f"Seleccionado ida y vuelta por un valor de ${frutillar *2}")
            recaudado+= frutillar*2
        else:
            print("Opcion no valida")
    else:
        print("Opcion no valida intente otra vez")
    respuesta=input("¿Quieres seguir vendiendo?  presione 1 para seguir vendiendo o presione cualquier boton para terminar ")
    if respuesta == "1":
        print("seguir vendiendo...")
    else:
        break

print(f"Se han recaudado ${recaudado}")
print("====FINALIZADO====")