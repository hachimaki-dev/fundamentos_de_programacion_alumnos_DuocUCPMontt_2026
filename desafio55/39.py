nombres = ['Juan', None, '', 'Ana', ' ']
nombres_validos = []
for i in nombres:
    if i is not None:
        limpieza = i.strip()
        if limpieza != '':
            nombres_validos.append(limpieza)
print(nombres_validos)