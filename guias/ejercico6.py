print("Deberas ingresar el código de un producto")


while True:
    codigo_producto = input("Ingresa el código de un producto: ").upper()

    if len(codigo_producto) < 6 or " " in (codigo_producto):
        print("Debes ingresar un codigo con una longitud minima de 6 caracteres y sin espacios.")
        continue
    else:
        print("Muy bien, el código es valido.")
        break

print(f"El producto ha sido registrado con el código {codigo_producto}.")