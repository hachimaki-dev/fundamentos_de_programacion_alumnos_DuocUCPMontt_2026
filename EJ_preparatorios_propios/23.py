# Este ejercicio es uno pensado por mi que es la combinacion entre la parte A y B de el ejercicio 22

paciente_grande = 0
paciente_pequeño = 0
stock = 30
historial_reservas = 0
id_animales_registrados = []

print("==="*12)
print("AGENDA CLÍNICA VETERINARIA PATITAS")
print("==="*12)


while True:
    print("1. Ver horas disponibles \n2. Reservar hora(s) \n3. Cancelar hora(s) \n4. Ver historial de reservas \n5. Registrar animal \n6. Historial Animales Registrados \n7. Salir")
    print()

    try:
        opcion_a_realizar = int(input("Ingrese la opcion que va a realizar :    "))

        if opcion_a_realizar == 7:
            print(f"Stock Final : {stock}")
            print(f"Resumen Pacientes: \nPacientes Grandes : {paciente_grande} \Pacientes Pequeños : {paciente_pequeño}")
            break
        elif opcion_a_realizar == 1:
            print(f"Horas disponibles : {stock}")
        elif opcion_a_realizar == 2:
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
        elif opcion_a_realizar == 3:
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
        elif opcion_a_realizar == 4:
            print("==="*8)
            print("Historial de Reservas")
            print("==="*8)
            print()
            print(f"Las horas que estan reservadas son {historial_reservas}")
        elif opcion_a_realizar == 5:
            while True:
                try:
                    animales_registrados = int(input("Ingrese cuantos animales se van a registrar :     "))
                    if animales_registrados <= 0:
                        print("El numero ingresado debe de ser un numero entero positivo")
                    else:
                        break
                except ValueError:
                        print("Ingrese una opcion valida")


            for a in range(animales_registrados):

                while True:
                    id_animal = input("Ingrese el id de el animal :     ").upper()
                    if len(id_animal) < 6 or " " in id_animal:
                        print("Ingrese un id el cual tenga minimo 6 caracteres y sin espacios")
                    else:
                        id_animales_registrados.append(id_animal)
                        break

                while True:
                    try:
                        peso_animal = int(input("Ingrse el peso del Animal :    "))

                        if peso_animal > 25:
                            paciente_grande += 1
                            break
                        else:
                            paciente_grande += 1
                            break
                    except ValueError:
                        print("Ingrese una opcion valida ")
        elif opcion_a_realizar == 6:
            print("==="*8)
            print("Historial de Animales Reservados")
            print("==="*8)
            print()
            print(f"Resumen Pacientes: \nPacientes Grandes : {paciente_grande} \nPacientes Pequeños : {paciente_pequeño}")
    except ValueError:
        print("Ingrese una opcion valida")

