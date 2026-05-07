cliente = "postpago"
plan = 15
gasto = 18
gg_extra = 1000
if cliente == "postpago":
    if gasto > plan:
        print((gasto - plan) * gg_extra)
else:
    print("Sin saldo")