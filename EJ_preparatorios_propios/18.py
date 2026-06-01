tecnico_maestro = 0
tecnico_operario = 0
total_registrados = 0

while True:
    try:
        tecnicos_registran = int(input("Cuantos Tecnicos se Registraran :   "))
        if tecnicos_registran <= 0 :
            print("Ingrese una cantidad entera positiva")
            continue
        else:
            total_registrados += tecnicos_registran
            break
    except ValueError:
        print("Ingrese una opcion valida")
        continue



for t in range(tecnicos_registran):
    print()
    while True:
        
        codigo_de_tecnico = input("Ingrese su codigo :  ")
        if len(codigo_de_tecnico) < 6 or " " in codigo_de_tecnico:
            print("El codigo debe de contener minimo 6 caracteres y sin espacios")
            continue
        else:
            break
    
    while True:
        try:
            año_experiencia = int(input("Ingrese sus años de experiencia :  "))
            if año_experiencia < 0 :
                print("Ingrese un numero entero positivo ")
                continue    
            elif año_experiencia > 10 :
                tecnico_maestro += 1
                break
            else:
                tecnico_operario += 1
                break
        except ValueError:
            print("Ingrese una opcion valida ")
            continue



print(f"Los Tecnicos registrados son {total_registrados} los cuales Son : \nTecnicos Maestros : {tecnico_maestro} \nTecnicos Operarios : {tecnico_operario}")
