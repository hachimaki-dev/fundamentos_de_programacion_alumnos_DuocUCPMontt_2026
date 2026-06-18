# Ejercicio 22 — Sistema completo de gestión de una clínica veterinaria Parte A

animales = []

pacientes_grandes = 0
pacientes_pequenos = 0

while True:

    try:
        cantidad_animales = int(input("¿Cuántos animales se registrarán?: "))

        if cantidad_animales > 0:
            break

        print("Error: debe ser mayor que cero.")

    except ValueError:
        print("Error: debe ser un número entero.")

for i in range(cantidad_animales):

    print(f"\nAnimal {i + 1}")

    while True:

        identificador = input("Ingrese ID del animal: ")

        if len(identificador) >= 6 and " " not in identificador:
            break

        print("Inválido: mínimo 6 caracteres, sin espacios.")

    while True:

        try:
            peso = int(input("Ingrese peso en kg: "))

            if peso > 0:
                break

            print("Error: debe ser mayor que cero.")

        except ValueError:
            print("Error: debe ser un número entero.")

    if peso > 25:
        categoria = "Paciente Grande"
        pacientes_grandes += 1
    else:
        categoria = "Paciente Pequeño"
        pacientes_pequenos += 1

    animal = {
        "id": identificador,
        "peso": peso,
        "categoria": categoria
    }

    animales.append(animal)

print()
print(f"La clínica ha registrado {pacientes_grandes} pacientes grandes y {pacientes_pequenos} pacientes pequeños. ¡Bienvenidos!")