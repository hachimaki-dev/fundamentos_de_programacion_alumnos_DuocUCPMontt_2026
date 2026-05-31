while True:
    try:
        pacientes_por_dia = int(input("Ingrese la cantidad de animales a atender : "))
        if pacientes_por_dia <= 0:
            print("ERROR, debe ser una cantidad válida, sobre 0.")
        else:
            print(f"Animales a atender hoy: {pacientes_por_dia}")
            break
    except ValueError:
        print("ERROR, debe ingresar valores númericos.")
clasificacion_pacientes = {}
clasificacion_pacientes["Paciente grande"] = 0
clasificacion_pacientes["Paciente pequeño"] = 0
for paciente in range(1, pacientes_por_dia+1):
    while True:
        try:
            ID_paciente = input(f"Ingrese el Id del paciente n°{paciente}: ")
            if len(ID_paciente) < 6 or " " in ID_paciente:
                print("ERROR, el ID debe tener minimo 6 caracteres y no debe tener espacios.")
                continue
            else:
                print(f"ID registrado : {ID_paciente}.")
            peso_paciente = int(input(f"Ingrese el peso del paciente n°{paciente}: "))
            if peso_paciente < 0:
                print("Lo sentimos, no podemos registrar a este paciente, solo admitimos kilogramos, no gramos.")
                continue
            if peso_paciente > 25:
                print("Paciente grandesito")
                clasificacion_pacientes["Paciente grande"] += 1
                break
            elif peso_paciente <= 25:
                print("Paciente chiquito")
                clasificacion_pacientes["Paciente pequeño"] += 1
                break
        except ValueError:
            print("ERROR, debe ingresar numeros enteros para poder registrar el peso del paciente.")
print(f"La clínica ha registrado a {clasificacion_pacientes['Paciente grande']} pacientes grandecitos y a {clasificacion_pacientes['Paciente pequeño']} pacientes chiquitos.")