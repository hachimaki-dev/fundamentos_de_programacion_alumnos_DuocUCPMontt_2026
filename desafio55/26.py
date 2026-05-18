imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
hojas_impresora = 5
for hoja in imprimir:
    if hoja == "TEXTO":
        hojas_ocupadas = 1
    elif hoja == "FOTO":
        hojas_ocupadas = 3
    if hojas_impresora < hojas_ocupadas:
        print("Sin papel")
        break
    print("Imprimiendo " + hoja)
    hojas_impresora -= hojas_ocupadas
