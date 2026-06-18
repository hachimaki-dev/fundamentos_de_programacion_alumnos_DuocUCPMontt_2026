# Ejercicio 5 — Código de producto en una bodega

while True:

    codigo = input("Ingrese el código del producto: ")

    if len(codigo) >= 6 and " " not in codigo:
        print(f"Producto registrado con código: {codigo}")
        break

    else:
        print("Código inválido. Debe tener al menos 6 caracteres y no contener espacios.")