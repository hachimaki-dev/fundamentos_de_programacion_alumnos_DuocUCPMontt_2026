codigo = (input("Cual es el codigo del producto: "))
    
if len(codigo) >= 6 and " " not in codigo:
    print(f"Producto registrado con código: {codigo}")
else:
    print("Codigo inválido. Debe tener al menos 6 caracteres y no contener espacios.")