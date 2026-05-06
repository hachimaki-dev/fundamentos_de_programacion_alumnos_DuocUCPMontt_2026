hojas_impresora = 5
impresiones = ["TEXTO","FOTO","TEXTO","FOTO"]
for i in impresiones:
    if hojas_impresora >= 3 and i == "FOTO":
        hojas_impresora = hojas_impresora - 3
        print(f"Imprimiendo {i}")
    elif hojas_impresora >= 1 and i == "TEXTO":
        hojas_impresora = hojas_impresora - 1
        print(f"Imprimiendo {i}")
    elif hojas_impresora <= 0:
        print("Sin papel")
        break
    