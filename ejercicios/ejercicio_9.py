aprobados = 0
revision_manual = 0
rechazados = 0

for i in range(8):

    while True:

        try:
            score = int(input(f"Ingrese el score de la solicitud {i + 1}: "))

            if 0 <= score <= 1000:
                break

            print("Error: el score debe estar entre 0 y 1000.")

        except ValueError:
            print("Error: debe ingresar un número entero.")

    if score > 750:
        print("Aprobado automáticamente")
        aprobados += 1

    elif score >= 500:
        print("Revisión manual")
        revision_manual += 1

    else:
        print("Rechazado")
        rechazados += 1

print()
print(f"Aprobados automáticamente: {aprobados}")
print(f"Revisión manual: {revision_manual}")
print(f"Rechazados: {rechazados}")