flag = True
while flag:
    codigo_de_producto = input("Ingrese el código del producto: ")
    if len(codigo_de_producto) < 6 or " " in codigo_de_producto:
        print("Código invalido. Debe tener minimo 6 caracteres y ningun espacio.")
    else:
        print(f"Código registrado : {codigo_de_producto}.")
        flag = False