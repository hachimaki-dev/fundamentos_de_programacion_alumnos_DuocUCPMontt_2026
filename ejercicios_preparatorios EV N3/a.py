
pacientes_grandes = 0
pacientes_pequeños = 0

while True:
    try:
        registro = int(input("¿Cuántos animales se registrarán?: "))
        if registro <= 0:
            print("Error: Debe registrar al menos 1 animal.\n")
            continue
        break  
    except ValueError:
        print("Error: Debe ingresar un número entero.\n")

print(f"\n--- Iniciando el registro de {registro} animales ---")


for i in range(registro):
    print(f"\n[ Registro Animal {i + 1} ]")
    

    while True:

        id_animal = input("Ingrese el ID del animal (Mínimo 6 caracteres): ")
        
        if len(id_animal) < 6:
            print("Error: El ID debe tener como mínimo 6 caracteres.")
        elif " " in id_animal:
            print("Error: El ID no puede contener espacios en blanco.")
        else:
            break  

    while True:
        try:
            peso = int(input("Ingrese el peso en kg: "))
            if peso <= 0:
                print("Error: El peso debe ser un número positivo mayor a 0.")
                continue
            break  
        except ValueError:
            print("Error: Debe ingresar un número entero para el peso.")

    if peso > 25:
        print(f"-> Clasificación: Paciente Grande")
        pacientes_grandes += 1  
    else:
        print(f"-> Clasificación: Paciente Pequeño")
        pacientes_pequeños += 1  

print("\n========================================================================")
print(f"La clínica ha registrado {pacientes_grandes} pacientes grandes y {pacientes_pequeños} pacientes pequeños. ¡Bienvenidos!")
print("========================================================================")