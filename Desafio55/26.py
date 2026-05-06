hojas = 5
impresiones = ["TEXTO", "FOTO", "TEXTO", "FOTO"]
for impresion in impresiones:
    if impresion == "TEXTO":
        hojas = hojas - 1
        if hojas <= 0:
            print("hola")
            break
    elif impresion == "FOTO":
        hojas = hojas - 3
        if hojas <= 0:
            print("huasd")
            break
