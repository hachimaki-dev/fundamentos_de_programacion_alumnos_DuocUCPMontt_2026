password = input("")

if len(password) < 6 or " " in password:
    print("Por favor ingrese una contraseña valida, debe tener al menos 6 caracteres o hay espacios")
else:
    print("Esta bacán la password")