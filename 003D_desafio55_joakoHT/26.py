hojas = 5
documentos = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for doc in documentos:
    if doc == 'TEXTO':
        costo = 1
    else:  # FOTO
        costo = 3

    if hojas < costo:
        print('Sin papel')
        break

    hojas -= costo
    print(f'Imprimiendo {doc}')