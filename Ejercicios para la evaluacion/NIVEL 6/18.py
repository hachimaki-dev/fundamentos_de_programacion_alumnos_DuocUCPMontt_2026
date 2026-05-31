while True:
    try:
        cantidad_de_tecnicos = int(input("Registre cuantos tecnicos de mantención hay: "))
        if cantidad_de_tecnicos <= 0:
            print("ERROR, debe ingresar una cantidad válida, solo numeros enteros positivos.")
        else:
            print(f"Cantidad de tecnicos registrados : {cantidad_de_tecnicos}.")
            break
    except ValueError:
        print("ERROR debe ingresar números enteros.")
tecnico_maestro = 0
tecnico_operario = 0
for tecnico in range(1, cantidad_de_tecnicos+1):
    while True:
        try:
            codigo_de_tecnico = input("Ingrese el código del tecnico actual: ")
            años_de_experiencia_tecnico = int(input("Ingrese los años de experiencia que lleva el tecnico: "))
            if años_de_experiencia_tecnico < 0:
                print("ERROR, no puedes ingresar números negativos como años de experiencia.")
            else:
                print(f"Años de experiencia registrado : {años_de_experiencia_tecnico}")

            if len(codigo_de_tecnico) < 6 or " " in codigo_de_tecnico:
                print("ERROR, el codigo debe tener minimo 6 caracteres y no tener espacios.")
            else:
                print(f"Código registrado del técnico : {codigo_de_tecnico}")
                break
        except ValueError:
            print("ERROR, en los años de experiencia debe de ingresar numeros enteros.")
    if años_de_experiencia_tecnico > 10:
        print("Este tecnico lleva más de 10 años de experiencia, debe ser tecnico maestro.")
        tecnico_maestro+=1
    elif años_de_experiencia_tecnico <= 10:
        print("Este tecnico es un tecnico operario.")
        tecnico_operario+=1
print(f"La planta cuenta con {tecnico_operario} tecnicos operarios y {tecnico_maestro} tecnicos maestros.")