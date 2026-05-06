tipo = "postpago"
gasto = 18
if tipo == "postpago":
    if gasto >= 15:
        cobro = (gasto - 15) * 1000
        print(cobro)
if tipo == "prepago":
    if gasto >= 15:
        print("sin saldo")