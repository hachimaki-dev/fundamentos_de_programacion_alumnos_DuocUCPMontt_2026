while True:
    try:
        medicamento = int(input('Ingresa cantidad de medicamentos disponible: '))
        if medicamento >= 1:
            break
        else:
            print('Dato invalido ingresa un numeroposivo para el stok')
    except ValueError:
        print('Dato invalido')
print(f"Stock registrado: {medicamento} unidades disponibles.")        