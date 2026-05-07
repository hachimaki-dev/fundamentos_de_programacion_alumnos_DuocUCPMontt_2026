respuestas = ['Juan', None, '', 'Ana', ' ']
datos_limpios = []
for elem in respuestas:
    if elem is not None and elem.strip() != '':
        datos_limpios.append(elem)
print(datos_limpios)