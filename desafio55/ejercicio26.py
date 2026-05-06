hojas_impresora = 5
a_imprimir = ["TEXTO", "FOTO", "TEXTO", "FOTO"]

while hojas_impresora > 0:
    for i in a_imprimir:
        if i == "TEXTO":
            hojas_impresora -= 1
        elif i == "FOTO":
            hojas_impresora -= 3

        print("Imprimiendo....")
        print(f"Quedan {hojas_impresora} hojas disponibles.")
        if hojas_impresora == 0:
            print("Ya no quedan hojas disponibles.")
            break
