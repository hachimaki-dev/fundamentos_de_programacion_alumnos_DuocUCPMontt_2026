respuestas = ['Juan', None, '', 'Ana', ' ']
nombres_limpios = []

for nombre in respuestas:
    if nombre is not None:
        nombre_procesado = nombre.strip()

        if nombre_procesado != "":
            nombres_limpios.append(nombre_procesado)

print(nombres_limpios)