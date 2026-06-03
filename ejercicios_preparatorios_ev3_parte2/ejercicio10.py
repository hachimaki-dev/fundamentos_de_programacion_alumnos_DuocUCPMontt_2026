pacientes = [{"nombre": "Ana", "edad": 28},
            {"nombre": "Juan", "edad": 30},
            {"nombre": "Carlos", "edad": 16}]

buscar_paciente = input("¿Que paciente desea buscar?: ").strip()
encontrado = False

for paciente in pacientes:
    if paciente["nombre"].lower() == buscar_paciente.lower():
        print("--- Paciente encontrado ---")
        print(f"Nombre: {paciente["nombre"]} | Edad: {paciente["edad"]}")
        encontrado = True
        break

if not encontrado:
    print("Paciente no encontrado.")
      