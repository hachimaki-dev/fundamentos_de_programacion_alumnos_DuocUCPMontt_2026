# Nombre de usuario para una app bancaria
# Un banco digital pide al usuario crear un nombre de usuario. Las reglas son:
# Mínimo 6 caracteres
# Sin espacios
# Si no cumple, muestra:
# "Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios."
# Ejemplos válidos: juanp23, mariatorres, cliente99 Ejemplos inválidos: juan, maria torres, ok
# Cuando sea válido:
# "Usuario creado: juanp23"
lista_contraseñas = {}
while True:
    try:
        nombre_usuario = str(input("Ingrese el nombre de usuario \n"))
        if len(nombre_usuario) >=6 and " " not in nombre_usuario:
            print(f"Usuario creado : {nombre_usuario}")
            lista_contraseñas["contraseña"] = nombre_usuario
            print(lista_contraseñas)
            break
        else:
            print("Nombre de usuario invalido , debe tener 6 caracteres minimo y sin espacios")
    except Exception as error_de_escritura:
        print(f"Ocurrio un error inesperado {error_de_escritura}")
