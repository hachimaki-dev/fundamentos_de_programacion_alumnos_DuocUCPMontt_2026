usuario = input("Crea tu nombre de usuario: ")

try:
    if len(usuario) < 6 or " " in usuario:
        raise ValueError
    
    print(f"Usuario creado: {usuario}")

except ValueError:
    print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")