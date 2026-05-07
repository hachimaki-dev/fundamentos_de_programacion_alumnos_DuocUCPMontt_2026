impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']
hojas = 5
for i in impresion:
    if i == "TEXTO":
        print("IMPRIMIENDO TEXTO")
        hojas -= 1
        if hojas <= 0:
            print("SIN PAPEL")
            break
    
    elif i == "FOTO":
        print("IMPRIMIENDO FOTO")
        hojas -= 3
        if hojas <= 0:
            print("SIN PAPEL")
            break