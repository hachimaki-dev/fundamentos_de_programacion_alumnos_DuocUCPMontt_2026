hojas_disponibles = 5
impresiones_solicitadas = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

for documento in impresiones_solicitadas:
    if documento == "TEXTO":
        documento = 1
        if hojas_disponibles >= documento:
            hojas_disponibles -= documento
            print("Imprimiendo TEXTO")
        else:
            print("Sin papel suficiente")
            break
    elif documento == "FOTO":
        documento = 3
        if hojas_disponibles >= documento:
            hojas_disponibles -= documento
            print("Imprimiendo FOTO")
        else:
            print("Sin papel suficiente")
            break