while True:
    try:
        equipos = int(input("Ingrese la cantidad de computadoras a registrar: "))
        if equipos > 0:
            break
        else:
            print("ERROR, debe ser entero positivo")
    except ValueError:
        print("ERROR, debe ser entero positivo")

equipo_obs = 0
equipo_vig = 0

for i in range(equipos):
    print(f"Computador {i + 1}")

    while True:
        codigo = input("Codigo de activo: ")
        if len(codigo) >= 6 and " " not in codigo:
            break
        else:
            print("ERROR, debe ser min 6 caracteres y sin espacios")
        
    while True:
        try:
            año = int(input("Ingrese año de fabricacion (1990 a 2026): "))
            if 1990 <= año <= 2026:
                break
            else:
                print("ERROR, El año debe estar entre 1990 a 2026")
        except ValueError:
            print("ERROR, debe ingresar un numero entero")
        

    if año >= 2018:
        print("Equipo Vigente")
        equipo_vig += 1
    else:
        print("Equipo Obsoleto")
        equipo_obs += 1

print(f"Equipos Vigentes: {equipo_vig}")
print(f"Equipos Obsoletos: {equipo_obs}")