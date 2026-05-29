while True:
    nombre = input("Ingrese nombre: ")
    if len(nombre) >= 6 and " " not in nombre:
        break
    else:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

print(f"Usuario creado: {nombre}")

 