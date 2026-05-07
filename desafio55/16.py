tipo_cliente = "Postpago"
plan_gb = 15
gb_usados = 18
recargo = 0
if tipo_cliente == "Postpago":
    if gb_usados > plan_gb:
        gigas_extra = gb_usados - plan_gb
        recargo = gigas_extra * 1000
else:
    print("Sin saldo")
print(recargo)