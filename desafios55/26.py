hojas_disponibles = 5
documentos = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for doc in documentos:

    if doc == 'TEXTO':
        costo = 1
    else:
        costo = 3
    
    if hojas_disponibles >= costo:
        hojas_disponibles -= costo
        print('Imprimiendo', doc)
    else:
        
        print('Sin papel')
        break