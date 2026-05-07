hojas_impresora = 5

loquese_imprime = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

for impresion in loquese_imprime:

    if impresion == "TEXTO":

        if hojas_impresora < 1:
            print("SIN PAPEL")
            break

        print("SE IMPRIMIO UN TEXTO")
        hojas_impresora -= 1

    elif impresion == "FOTO":

        if hojas_impresora < 3:
            print("SIN PAPEL")
            break

        print("SE IMPRIMIO UNA FOTO")
        hojas_impresora -= 3