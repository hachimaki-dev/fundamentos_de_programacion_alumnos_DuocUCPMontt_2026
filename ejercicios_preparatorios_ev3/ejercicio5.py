while True:
    producto_registrado = input("Ingrese su producto: ")

    if len(producto_registrado) >= 6 and " " not in producto_registrado:
        print(f"Producto registrado con código: {producto_registrado}")
        break
    else:
        print("Producto invalido, debe tener al menos 6 caracteres y sin espacios")