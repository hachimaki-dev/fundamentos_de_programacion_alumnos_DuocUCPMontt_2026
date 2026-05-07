datos_sucios = ['Juan', None, '', 'Ana', ' ']
datos_limpios = []

for item in datos_sucios:
   
    if item is not None:
       
        item_limpio = item.strip()
        
       
        if item_limpio != '':
            datos_limpios.append(item_limpio)

print(datos_limpios)
