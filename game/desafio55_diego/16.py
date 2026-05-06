tipo = "Postpago"
plan_gigas = 15
uso_gigas = 18

if tipo == "Postpago":
    if uso_gigas > plan_gigas:
        recargo = (uso_gigas - plan_gigas) *1000
    else:
        recargo = 0
    print(recargo)
else:
    print("Sin Saldo")