while True:
    codigo = input("introduce el código del producto: ")
    if len(codigo) >= 6 and not " " in codigo:
        print(f"producto registrado: {codigo}")
        break
    else:
        print("Código inválido. Debe tener al menos 6 caracteres y no contener espacios.")