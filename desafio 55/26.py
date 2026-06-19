hojas = 5

documentos = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for documento in documentos:
    
    if documento == 'TEXTO':
        gasto = 1
    else:
        gasto = 3

    if hojas < gasto:
        print("Sin papel")
        break

    print("Imprimiendo", documento)
    
    hojas = hojas - gasto