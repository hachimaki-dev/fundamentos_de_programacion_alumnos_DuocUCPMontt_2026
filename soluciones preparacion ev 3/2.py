medicamentos_disponibles = 0

while medicamentos_disponibles <= 0 :
    try :
        medicamentos_disponibles = int(input("Ingrese la cantidad de medicamentos disponibles: "))

        if medicamentos_disponibles > 0 :
            break
        else :
            print("Dato inválido. Ingresa un entero positivo para el stock.")
    except ValueError :
        print("Dato inválido. Ingresa un entero positivo para el stock.")

print(f"Stock registrado: {medicamentos_disponibles} unidades disponibles.")