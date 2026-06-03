pacientes = 3
datos_pacientes = []

for p in range(pacientes):
    
    while True:
        
        nombre_paciente = input("Ingrese su Nombre :    ")
        if len(nombre_paciente) <= 0:
            print("Ingrese su nombre correctamente , no deje vacio")
            print()
        else:
            break
    
    while True:
        try:
            edad_paciente = int(input("Ingrse su edad :     "))
            if edad_paciente <= 0:
                print("ingrese un numero entero positivo ")
                print()
            else:
                break
        except ValueError:
            print("Ingrse una opcion valida")
            print()

    datos = {"nombre": nombre_paciente, "edad": edad_paciente}
    datos_pacientes.append(datos)

print()
for p in datos_pacientes:
    print(f"Nombre: {p["nombre"]} | Edad: {p["edad"]}")

