hojas_impresora = 5
impresiones = ["texto","foto","texto","foto"]
contador = 0
for i in impresiones:
    if i == "texto":
        if hojas_impresora >= 1:
            print(f"imprimiendo {i}")
            hojas_impresora = hojas_impresora - 1
        else:
            print("SIN PAPEL")
            break

    elif i == "foto":
        if hojas_impresora >= 3:
            print(f"imprimiendo {i}")
            hojas_impresora = hojas_impresora - 3
        else:
            print("SIN PAPEL")
            break
    contador = contador + 1