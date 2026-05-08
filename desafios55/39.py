formulario1 = ['Juan', None, '', 'Ana', ' ']
lista_blanca = []

for formulario in formulario1:
    
    if formulario is not None and formulario.strip() != "":
        lista_blanca.append(formulario)
        
print(lista_blanca)
        
