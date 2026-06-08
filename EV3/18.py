maestros = 0
operarios = 0

while True:
    try:
        n = int(input("¿Cuántos técnicos se registrarán? "))
        if n <= 0:
            print("Error: debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Error: ingrese un número entero.")

for i in range(n):
    print(f"\n--- Técnico {i+1} ---")

    while True:
        codigo = input("Código del técnico: ")
        if len(codigo) < 6:
            print("Error: el código debe tener mínimo 6 caracteres.")
        elif " " in codigo:
            print("Error: el código no puede tener espacios.")
        else:
            break

    while True:
        try:
            anios = int(input("Años de experiencia: "))
            if anios <= 0:
                print("Error: debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Error: ingrese un número entero.")

    if anios > 10:
        print("Clasificación: Técnico Maestro")
        maestros += 1
    else:
        print("Clasificación: Técnico Operario")
        operarios += 1

print(f"\nLa planta cuenta con {maestros} Técnicos Maestros y {operarios} Técnicos Operarios. Sistema listo.")