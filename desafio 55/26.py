hojas_impresora = 5
impresiones = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
foto = 3
texto = 1

for doc in impresiones:
    if doc == "TEXTO":
        costo = texto
    else:
        costo = foto

    if hojas_impresora < costo:
        print("Sin papel")
        break

    hojas_impresora -= costo
    print("Imprimiendo", doc)
