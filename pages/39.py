nombre_sucios = ['Juan', None, '', 'Ana', ' ', '     ', 'Pepe', None, 'Lucho']

nombres_limpios = []

for nombre in nombre_sucios:
    if nombre is None:
        continue
    elif nombre is not None and len(nombre.strip()) != 0:
        nombres_limpios.append(nombre)
print(nombres_limpios)