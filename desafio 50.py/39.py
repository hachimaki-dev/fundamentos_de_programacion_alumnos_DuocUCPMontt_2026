nombres_sucios=['Juan', None, '', 'Ana', ' ']

nombres_limpios=[]

for nombre in nombres_sucios:
    if nombre is None:
        continue
    elif nombre is not None and len (nombre.strip()) !=0:
        nombres_limpios.append(nombre)
print(nombres_limpios)
