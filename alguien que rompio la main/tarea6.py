while True:
    codigo = input("Ingrese el código del producto: ")
    
    if len(codigo) >= 6 and " " not in codigo:
        
        print(f"Producto registrado con código: {codigo}")
        break
    else:
        print("Código inválido. Intente nuevamente.")