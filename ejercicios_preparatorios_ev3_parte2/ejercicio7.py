pacientes = []

for i in range(3):
    print(f"Registrar paciente numero {i+1}.")
    while True:
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
            if len(nombre_paciente) >= 0:
                break
            print("El nombre no puede estar vacio.")

    while True:
        try:
            edad_paciente = int(input("Ingrese la edad del paciente: "))
            if edad_paciente <= 0:
                print("Ingrese un numero positivo")
            else:
                print("La edad se ha ingresado correctamente.")
                break
        except ValueError:
            print("Dato invalido: Ingrese un numero positivo")
    
    paciente = {"nombre": nombre_paciente, "edad": edad_paciente}
    pacientes.append(paciente)

print("\n--- Lista de Pacientes ---")
for paciente in pacientes:
    print(f"Nombre: {paciente["nombre"]} | Edad: {paciente["edad"]}")