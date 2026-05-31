aforo_evento_musica = 500
total_ingresados = 0

print("==="*12)
print("CONTROL DE ACCESO - FESTIVAL AUSTRAL")
print("==="*12)

while True:
    print("1. Ver cupos disponibles \n2. Registrar entrada de grupo \n3. Registrar salida de grupo \n4. Total de personas que han ingresado \n5. Salir")    
    print()

    try:
        opcion_elejida = int(input("Ingrese la opcion que va a realizar :  "))

        if opcion_elejida == 5:
            print(f"Cupos Disponibles : {aforo_evento_musica}")
            print()
            break
        elif opcion_elejida == 1:
            print(f"Cupos Disponibles : {aforo_evento_musica}")
            print()
        elif opcion_elejida == 2:
            while True:
                try:
                    entrada_de_grupo = int(input("Cuantas personas van a entrar: "))
                    if entrada_de_grupo > aforo_evento_musica:
                        print("No hay espacio para la cantidad ingresada ")
                        continue
                    else:
                        aforo_evento_musica -= entrada_de_grupo
                        total_ingresados += entrada_de_grupo
                        print(f"Cupos disponibles : {aforo_evento_musica}")
                        print()
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_elejida == 3:
            while True:
                try:
                    salida_de_grupo = int(input("Cuantas personas van a Salir:   "))
                    if salida_de_grupo > 500:
                        print("No pueden salir mas de los cupos disponibles")
                        continue
                    else:
                        aforo_evento_musica += salida_de_grupo
                        print(f"Cupos disponibles : {aforo_evento_musica}")
                        print()
                        break
                except ValueError:
                    print("Ingrese una opcion valida")  
        elif opcion_elejida == 4:
            print("==="*14)
            print("Total de personas que han ingresado")
            print("==="*14)
            print()
            print(f"El total de Personas que han Ingresado hoy :  {total_ingresados}")
            print()
    except ValueError:
        print("Ingrese una opcion valida")
