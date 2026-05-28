while True:
    codigo = input("ingrese el codigo del producto: ")
    if len(codigo) >= 6 and " " not in codigo:
        print(f"producto registrado con codigo: {codigo}")
        break
    else:
        print("codigo inválido. Debe tener al menos 6 caracteres y no contener espacios.")