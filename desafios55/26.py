hojas = 5
cola = ["texto", "foto", "texto", "foto"]
for documento in cola:
    if documento == "texto":
        if hojas >= 1:
            print("imprimiendo " + documento )
            hojas -= 1
        else:
            print("sin papel")
            break
    else:
        if hojas >= 3:
            print("imprimiendo " + documento)
            hojas -= 3
        else:
            print("sin papel")
            break