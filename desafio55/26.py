Hojas = 5
cola_impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
for documento in cola_impresion:
    if documento == "TEXTO":
        costo = 1
    elif documento == "FOTO":
        costo = 3
    if Hojas >= costo:
        Hojas -= costo
        print(F"Imprimiendo {documento}")
    else:
        print("Sin papel")
        break
    