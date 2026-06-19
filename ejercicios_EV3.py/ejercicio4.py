while True:
    nombre = input('Crea tu nombre de usuario:').strip()
    if len(nombre) >= 6 and ' ' not in nombre:
        break
    else:
        print('Nombre invalido. Debe tener al menos 6 caracters y no conttener espacio')
print('Usuario creado :', nombre)