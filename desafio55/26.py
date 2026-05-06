hojas_restantes_impresora = 5
cola_de_impresion = [ "TEXTO", "FOTO", "TEXTO", "FOTO" ]

for i in cola_de_impresion:
    if i == "TEXTO" and hojas_restantes_impresora >= 1:
        print(f"Imprimiendo {i}")
        hojas_restantes_impresora = hojas_restantes_impresora - 1
    elif i == "FOTO" and hojas_restantes_impresora >= 3:
        print(f"Imprimiendo {i}")
        hojas_restantes_impresora = hojas_restantes_impresora - 3
    else:
        print("Sin papel")
        break
