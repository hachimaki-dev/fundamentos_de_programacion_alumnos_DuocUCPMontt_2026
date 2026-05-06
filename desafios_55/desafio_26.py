hojas_disponibles = 5
cola_de_impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

for documento in cola_de_impresion:
    if documento == "TEXTO" and hojas_disponibles >= 1:
        hojas_disponibles -= 1
        print("Imprimiendo texto")
    elif documento == "FOTO" and hojas_disponibles >= 3:
        hojas_disponibles -= 3
        print("Imprimiendo foto")
    else:
        print("Sin papel")