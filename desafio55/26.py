cola_impresion = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
texto = 1
foto = 3
hojas = 5
for impresion in cola_impresion:
    if hojas == 0:
        print("Sin papel")
        break
    elif impresion == "TEXTO":
        if hojas >= 1:
            print(f"Imprimiendo {impresion}")
            hojas -= 1
    elif impresion == "FOTO":
        if hojas >= 3:
            print(f"Imprimiendo {impresion}")
            hojas -= 3