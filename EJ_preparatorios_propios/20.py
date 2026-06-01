stock = 60
total_prestamos = 0

print("==="*14)
print("BIBLIOTECA TECNOLÓGICA UNIVERSIDAD DEL SUR")
print("==="*14)


while True:
    print()
    print("1. Ver equipos disponibles \n2. Prestar equipo(s) \n3. Recibir devolución \n4. Ver historial de préstamos activos \n5. Salir")
    print()
    try:
        opcion_elegida = int(input("Ingrese la Opcion a Realizar :   "))
        
        if opcion_elegida == 5:
            print(f"Stock final : {stock} \nGracias por utilizar el sistema. Hasta pronto.")
            break
        elif opcion_elegida == 1:
            print(f"Stock :  {stock}")
        elif opcion_elegida == 2:
            while True:
                try:
                    prestar_equipos = int(input("Cuantos equipos desea Prestar :   "))
                    if prestar_equipos > stock:
                        print("El prestamo no puede superar el stock actual")
                    else:
                        stock -= prestar_equipos
                        total_prestamos += prestar_equipos
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_elegida == 3:
                while True:
                    try:
                        devolucion_equipos = int(input("Cuantos equipos desea Devolver :   "))
                        if devolucion_equipos > total_prestamos:
                            print("Los equipos a devolver no pueden ser mas de los que se prestaron")
                        else:
                            stock += devolucion_equipos
                            total_prestamos -= devolucion_equipos
                            break
                    except ValueError:
                        print("Ingrese una opcion valida")
        elif opcion_elegida == 4:
            print()
            print("#####"*10)
            print("Historial de Prestamos Activos ")
            print("#####"*10)
            print()
            print(f"Los prestamos que se an realizado son {total_prestamos}")
            print()
        else:
            print("Ingrese uan opcion valida")
    except ValueError:
        print("Ingrese una opcion valida")