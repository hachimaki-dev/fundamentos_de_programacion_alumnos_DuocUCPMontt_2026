nombres_respuestas = ['Juan', None, '', 'Ana', ' ']
nombres_validos = []
for elem in nombres_respuestas:
    if elem is not None and elem.strip() != "":
        nombres_validos.append(elem.strip())
print(nombres_validos)