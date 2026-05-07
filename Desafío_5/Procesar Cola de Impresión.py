Impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
Hojas = 5

for Impresion in Impresion:

    if Impresion == "FOTO":
        costo = 1

    elif Impresion == "TEXTO":
        costo = 3

    
    if Hojas < costo:
        print ("Sin papel")
        break

    print (f"Imprimiendo {Impresion}")

    Hojas -= costo

print (f"Hojas restante: {Hojas}")