nombres_sucios = ['Juan', None, '', 'Ana', '']
contador = 0
for i in nombres_sucios:
    if i is not None and i.strip() != "":
        continue
    else:
        nombres_sucios.pop(contador)
    contador += 1
print(nombres_sucios)
    
        