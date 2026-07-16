nombres_sucios = ['Juan', None, '', 'Ana ', '']
contador = 0
nombres_limpios = []
for i in nombres_sucios:
    if i is None:
        continue
    elif len(i) == 0:
        continue
    else:
        nombres_limpios.append(i.strip())
    
print(nombres_limpios)