respuestas = ['Juan', None, '', 'Ana', "T"]
limpias = []
 
for elem in respuestas:
    if elem is not None and elem.strip() != '':
        limpias.append(elem)
 
print(limpias)
print()