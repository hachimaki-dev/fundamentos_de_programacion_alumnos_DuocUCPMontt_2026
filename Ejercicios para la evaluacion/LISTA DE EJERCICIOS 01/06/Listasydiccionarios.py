datos_pacientes = {}
for dato in range(1,4):
    while True:
        nombre_del_paciente = input(f"Ingrese el nombre del paciente n°{dato}: ").strip()
        if len(nombre_del_paciente) > 0:
            print(f"Registro nombre: {nombre_del_paciente}")
            break
        else:
            print("No puede dejar vacio el nombre.")
    
    while True:
        try:
            edad_paciente = int(input("Ingrese la edad del paciente: "))
            if edad_paciente <= 0:
                print("ERROR, no se puede ingresar una edad igual o menor a 0.")
            else:
                print(f"Edad registrada: {edad_paciente}.")
                break
        except ValueError:
            print("ERROR, la edad del paciente debe ser en numeros.")
    if (edad_paciente and nombre_del_paciente) not in (datos_pacientes):
        datos_pacientes[nombre_del_paciente] = edad_paciente
    else:
        print("Ya registrado.")
for nombre, edad in datos_pacientes.items():
    print(f"Nombre: {nombre} | Edad: {edad} ")