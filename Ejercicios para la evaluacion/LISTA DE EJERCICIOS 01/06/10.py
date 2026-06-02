registro_de_pacientes = [{"nombre": "juan", "edad": 34}, {"nombre": "Lucia", "edad":55}, {"nombre": "Pepe", "edad": 33}]
buscar_paciente = input("Ingrese el nombre del paciente: ").strip()
flag = False
for paciente in registro_de_pacientes:
    if paciente["nombre"].lower() == buscar_paciente.lower():
        print(f"Paciente encontrado: {paciente["nombre"]} | Edad: {paciente["edad"]}")
        flag = True
        break
if not flag:
    print("Paciente no encontrado.")
    