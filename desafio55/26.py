hojas = 5
impresion = ["texto","foto","texto","foto"]
for i in impresion:
    if hojas <= 0:
        print("sin papel")
        break
    elif i == "texto":
        hojas -= 1
        print("imprimiendo texto")
    elif i == "foto":
        hojas -= 3
        print("imprimiendo foto")
    elif hojas <= 0:
        print("sin papel")
        break