respuestas = ['Juan', None, '', 'Ana', ' ']

lista_limpia = []

for nombre in respuestas:
    
    if nombre is not None and nombre.strip() != "":
        
        lista_limpia.append(nombre.strip())

print(lista_limpia)