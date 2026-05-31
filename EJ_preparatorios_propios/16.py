pacientes_en_sala = 0
ingreso = 0
alta = 0


print("===="*10)
print("URGENCIAS HOSPITAL REGIONAL")
print("===="*10)

while True:
    print("1. Ver pacientes en sala \n2. Registrar ingreso de paciente(s) \n3. Registrar alta de paciente(s)\n4. Total de ingresos del turno \n5. Salir")

    try:
        opcion_elegida = int(input("Ingrese que opcion desea realizar :  "))
        
        if opcion_elegida == 5:
            print(f"Pacientes en sala : {pacientes_en_sala}")
            break
        elif opcion_elegida == 1:
            print(f"Pacientes en sala : {pacientes_en_sala}")
        elif opcion_elegida == 2:
            while True:
                try:
                    registrar_entrada_pacientes = int(input("Ingrese cuantos pacientes van a entrar :  "))
                    if pacientes_en_sala + registrar_entrada_pacientes > 25:
                        print("El limite de pacientes en sala son 25 , no puede superar el limite")
                        continue
                    else:
                        pacientes_en_sala += registrar_entrada_pacientes
                        ingreso += registrar_entrada_pacientes
                        print(f"Pacientes en sala actualmente : {pacientes_en_sala}")
                        break
                except ValueError:
                    print("ingrese una opcion valida")
        elif opcion_elegida == 3:
            while True:
                try:
                    registrar_alta_pacientes = int(input("Ingrese cuantos pacientes van a dar de alta :   "))
                    if registrar_alta_pacientes > pacientes_en_sala or registrar_alta_pacientes > 25:
                        print("El limite de pacientes a dar a alta no puede superar el limite")
                        continue
                    else:
                        pacientes_en_sala -= registrar_alta_pacientes
                        alta += registrar_alta_pacientes
                        print(f"Pacientes en sala actualmente : {pacientes_en_sala}")
                        break
                except ValueError:
                    print("ingrese una opcion valida")
        elif opcion_elegida == 4:
            print("===="*12)
            print("Historial")
            print("===="*12)
            print()
            print(f"Pacientes en sala : {pacientes_en_sala} \nPacientes Ingresados en el turno de hoy : {ingreso} \nPacientes dados de alta : {alta}")
            print()
    except ValueError:
        print("Ingrse una opcion valida")
