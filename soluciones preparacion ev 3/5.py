nombre_codigo = ""

while True:
    try :
        nombre_codigo = str(input("Ingrese el código del producto: "))

        if len(nombre_codigo) > 5 and not " " in nombre_codigo:
            break
        else :
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
    except TypeError :
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

print(f"Producto registrado con código: {nombre_codigo}")