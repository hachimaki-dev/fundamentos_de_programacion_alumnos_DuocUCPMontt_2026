imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
hojas = 5
for imprime in imprimir:
    if imprime == "TEXTO":
        costo = 1
    else:
        costo = 3
    if hojas < costo:
        print("sin papel")
        break

    print("imprimendo", imprime)
    hojas -= costo