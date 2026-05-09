tipo = "Postpago"
plan_gb = 15
uso_gb = 18
recago = 0
extra = 0
if tipo == "Postpago":
    if uso_gb > plan_gb:
        extra = uso_gb - plan_gb
        recargo = extra * 1000
    else:
        recargo = 0
    print(recargo)
else:
    print("Sin saldo")