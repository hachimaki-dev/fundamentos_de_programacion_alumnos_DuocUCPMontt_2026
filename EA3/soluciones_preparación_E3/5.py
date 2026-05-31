usuario = input("Ingrese su nombre de usuario: ")
if len(usuario) >= 6 and " " not in usuario:
    print("usuario creado: " + usuario)
else:  
    print("nombre invalido: el nombre debe tener al menos 6 caracteres")