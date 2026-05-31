código_válido = False

while código_válido == False:
    codigo_a_registrar = input("Ingrese código de producto: ")
    if len(codigo_a_registrar) >= 6:
        if " " in codigo_a_registrar:
            print("Ingrese un código válido, sin espacios y con al menos 6 caracteres")
        else:
            código_válido = True
    else:
        print("Ingrese un código válido, sin espacios y con al menos 6 caracteres")

print(f"Producto registrado con código: {codigo_a_registrar}")

