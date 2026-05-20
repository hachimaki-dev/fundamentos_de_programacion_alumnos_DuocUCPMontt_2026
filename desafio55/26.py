para_imprimir = ["TEXTO","FOTO","TEXTO","FOTO"]
hojas = 5
for impresion in para_imprimir:
    if impresion == "TEXTO":
        if hojas <= 0:
            print("Sin papel")
            break
        hojas-=1
        print(f"Imprimiendo {impresion}")
    elif impresion == "FOTO":
        if hojas <= 0:
            print("Sin papel")
            break
        hojas -= 3
        print(f"Imprimiendo {impresion}")