hojas_impresora = 5
cosas_a_imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
contador_de_cosas = 0
for i in cosas_a_imprimir:
    if hojas_impresora > 0:
        if i == "TEXTO"and hojas_impresora >= 1:
            hojas_impresora = hojas_impresora - 1
            print(f"imprimiendo {cosas_a_imprimir[contador_de_cosas]}")
        elif i == "FOTO" and hojas_impresora >= 3:
            hojas_impresora = hojas_impresora - 3
            print(f"imprimiendo {cosas_a_imprimir[contador_de_cosas]}")
    else:
        print("SIN PAPEL")
        break
    contador_de_cosas += 1
