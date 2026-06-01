stock = 30
historial_reservas = 0

print("==="*12)
print("AGENDA CLÍNICA VETERINARIA PATITAS")
print("==="*12)

while True:
    print("1. Ver horas disponibles \n2. Reservar hora(s) \n3. Cancelar hora(s) \n4. Ver historial de reservas \n5. Salir")
    print()

    try:
        opcion_elegida = int(input("Ingrese la opcion que va a realizar :    "))

        if opcion_elegida == 5:
            print(f"Stock Final : {stock}")
            break
        elif opcion_elegida == 1:
            print(f"Horas Disponibles : {stock}")
        elif opcion_elegida == 2:
            while True:
                try:
                    reservar_hora = int(input("Ingrese cuantas horas va a reservar :    "))
                    if reservar_hora > stock:
                        print("No se pueden reservar mas horas de las que estan disponibles")
                    else:
                        stock -= reservar_hora
                        historial_reservas += reservar_hora
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_elegida == 3:
            while True:
                try:
                    cancelar_hora = int(input("Ingrese cuantas horas se vana  cancelar  :       "))
                    if cancelar_hora > historial_reservas:
                        print("No se pueden cancelar mas horas de las que estan reservadas")
                    else:
                        stock += cancelar_hora
                        historial_reservas -= cancelar_hora
                        break
                except ValueError:
                    print("Ingrese una opcion valida")
        elif opcion_elegida == 4:
            print("==="*8)
            print("Historial de Reservas")
            print("==="*8)
            print()
            print(f"Las horas que estan reservadas son {historial_reservas}")
    except ValueError :
        print("Ingrese uan opcion valida")


