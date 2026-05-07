hojas = 5
impresiones = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

costo_texto = 1
costo_foto = 3

for documento in impresiones:
    if documento == "TEXTO":
        gasto = costo_texto
    else:
        gasto = costo_foto

    if gasto <= hojas:
        print(f"Imprimiendo {documento}")
        hojas = hojas - gasto
    else:
        print("Sin papel")
        break