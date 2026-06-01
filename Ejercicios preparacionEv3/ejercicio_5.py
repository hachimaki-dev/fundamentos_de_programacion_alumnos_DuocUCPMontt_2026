while True:
    codigo = input("Ingrese el codigo de el producto (Ejemplo: P1234X): ")

    if len(codigo) < 6 or " " in codigo:
        print("Codigo invalido!, intente de nuevo.")
    # if codigo.count(" ") > 0:
    
    else:
        print(f"Codigo {codigo} registrado con exito!")
        break