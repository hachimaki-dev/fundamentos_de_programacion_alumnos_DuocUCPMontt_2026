while True:
    nombre_usuario = input("Ingrese tu nombre de usuario")
    if len(nombre_usuario) >= 6 and " " not in nombre_usuario:
        break
    else:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")
print(f"Usuario creado: {nombre_usuario}")
