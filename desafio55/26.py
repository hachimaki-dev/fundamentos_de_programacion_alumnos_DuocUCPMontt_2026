hojas = 5
imprimir = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']
for doc in imprimir:
    if doc == 'TEXTO':
        hojas_usadas = 1
    else:
        hojas_usadas = 3
    if hojas < hojas_usadas:
        print("Sin papel")
        break
    print("Imprimiendo", doc)
    hojas -= hojas_usadas