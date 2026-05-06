hojas_disponibles = 5
cola_impresion = ['Texto', 'Foto', 'Texto', 'Foto']

for documento in cola_impresion:
    if documento == "Texto" and hojas_disponibles >= 1:
        hojas_disponibles -= 1
        print("Imprimiendo texto")
    elif documento == "Foto" and hojas_disponibles >= 3:
        hojas_disponibles -= 3
        print("Imprimiendo foto")
    else:
        print("Sin papel")