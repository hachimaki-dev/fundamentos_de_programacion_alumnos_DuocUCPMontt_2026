
hojas_desponibles = 5

cola_de_impresion = ['TEXTO', 'FOTO', 'TEXTO', 'FOTO']

for documento in cola_de_impresion:
    if documento == 'TEXTO' and hojas_desponibles >=1:
        hojas_desponibles -= 1
        print("imprimiendo texto")
    elif documento == 'FOTO'and hojas_desponibles >= 3:
        hojas_desponibles -= 3 
        print("imprimiendo foto")
    else:
        print("sin papel")







