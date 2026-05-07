para_imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
hojas = 5

for impresion in para_imprimir:

    if impresion == "TEXTO":
        gasto = 1

    else:
        gasto = 3


    if hojas < gasto:
        print("Sin papel")
        break


    hojas = hojas - gasto
    print(f"Imprimiendo {impresion}")
