print("Bienvenido al Banco Estado, deberás crear un nombre de usuario para usar el servicio.")
print("Recuerda que el nombre de usuario debe tener como minimo 6 caracteres, y no contener espacios")

while True:
    nombre_usuario = input("Ingresa el nuevo nombre de usuario: ")

    if len(nombre_usuario) < 6 or " " in nombre_usuario:
        print("Nombre invalido, debe contener 6 caracteres como minimo y no contener espacios")
        continue
    else:
        print("Muy bien, el nombre de usuario esta correctamente escrito.")
        break

        


print(f"El nombre de usuario final es {nombre_usuario}")