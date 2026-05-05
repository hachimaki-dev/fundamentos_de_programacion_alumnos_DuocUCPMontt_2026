hojas_restantes = 5
cola = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

hojas_x_texto = 1
hojas_x_foto = 3

for impresion in cola:
    if impresion == "TEXTO":
        if hojas_restantes - hojas_x_texto >= 0:
            print("Imprimiendo TEXTO")
            hojas_restantes -= hojas_x_texto
        else:
            print("Sin papel")
    else:
        if hojas_restantes - hojas_x_foto >= 0:
            print("Imprimiendo FOTO")
            hojas_restantes -= hojas_x_foto
        else:
            print("Sin papel")