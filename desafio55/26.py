hojas_impresora = 5
lista_imprimiciones = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']


while hojas_impresora >= 1:
    for cada_elemento in range(len(lista_imprimiciones)):
        if lista_imprimiciones[cada_elemento] == "TEXTO" and hojas_impresora >= 1:
            print("Imprimiendo ", lista_imprimiciones[cada_elemento])   
            hojas_impresora -= 1
        elif lista_imprimiciones[cada_elemento] == "FOTO" and hojas_impresora >=3:
            hojas_impresora -= 3
            print("Imprimiendo", lista_imprimiciones[cada_elemento])
    if hojas_impresora <= 0:
        print("Sin hojas")
   

