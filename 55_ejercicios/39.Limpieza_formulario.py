respuestas_formulario = ['Juan', None, '', 'Ana', ' ']
respuestas_limpias = []
for elem in respuestas_formulario:
    if elem is not None and elem.strip() != '':
        respuestas_limpias.append(elem)
print(respuestas_limpias)