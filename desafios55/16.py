tipo_cliente = "postpago"
plan_gb = 15
gastado_gb = 18
if tipo_cliente == "postpago":
    if gastado_gb > plan_gb:
        recargo = (gastado_gb - plan_gb) * 1000
        print(recargo)
    else:
        print(0)
else:
    print("sin saldo")