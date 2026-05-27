# Ejercicio 4 — Nombre de usuario para una app bancaria
# Un banco digital pide al usuario crear un nombre de usuario. Las reglas son:

# Mínimo 6 caracteres
# Sin espacios
# Si no cumple, muestra:

# "Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios."
# Ejemplos válidos: juanp23, mariatorres, cliente99 Ejemplos inválidos: juan, maria torres, ok

# Cuando sea válido:

# "Usuario creado: juanp23"

while True:
    usuario_ingresado = input("Cree su usuario: ")

    if len(usuario_ingresado) < 6:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

    elif " " in usuario_ingresado:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

    else:
        print(f"Usuario creado: {usuario_ingresado}")
        break