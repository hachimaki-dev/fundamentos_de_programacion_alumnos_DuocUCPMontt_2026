tipo_cliente = "Postpago"
plan_gb = 15
gasto_gb = 18
recargo_final = 0
if tipo_cliente == "Postpago":
    if gasto_gb > plan_gb:
        gigas_extras = gasto_gb - plan_gb
        recargo_final = gigas_extras * 1000
elif tipo_cliente == "prepago":
    print("Sin saldo")
print(recargo_final)