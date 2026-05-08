data_science = ['Juan', 'None', 'Ana', '']
lista_limpia = []
for elem in data_science:
    if elem is not 'None' and elem.strip() != '':
        lista_limpia.append(elem)
print(lista_limpia)
