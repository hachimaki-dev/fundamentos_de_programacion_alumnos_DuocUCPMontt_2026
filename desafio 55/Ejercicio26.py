cola_de_impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
hojas_disponibles = 5

for documento in cola_de_impresion:
    if documento == "TEXTO" and hojas_disponibles >= 1:
        print(f"Imprimiendo Texto")
        hojas_disponibles = hojas_disponibles - 1
    elif documento == "FOTO" and hojas_disponibles >= 3:
        print(f"Imprimiendo foto")
        hojas_disponibles = hojas_disponibles - 1
    else:
        print(f"Hojas insuficientes")