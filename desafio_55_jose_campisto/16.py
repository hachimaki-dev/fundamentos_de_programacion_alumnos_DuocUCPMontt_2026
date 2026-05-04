cliente="Postpago"
plan=15
exceso=3
cobro=0
if cliente == "Postpago":
    if exceso != 0:
        cobro= 1000*exceso
        print(cobro)
else:
    print("Sin saldo")