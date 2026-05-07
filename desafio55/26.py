impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']
hojas = 5
for i in impresion:
    if i in ["TEXTO"]:
        hojas -= 1
        if hojas > 0:
            print("TEXTO")
        else:
            print("SIN PAPEL")
            break
    if i in ["FOTO"]:
        hojas -= 3
        if hojas > 0:
            print("FOTO")
        else:
            print("SIN PAPEL")
            break