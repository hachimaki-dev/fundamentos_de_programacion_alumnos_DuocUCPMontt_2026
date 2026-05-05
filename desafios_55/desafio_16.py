tipo_cliente = "Postpago"
gb_plan = 15
gb_consumidos = 18
precio_gb_extra = 1000

if tipo_cliente == "Postpago":
    if gb_consumidos > gb_plan:
        gb_extras = gb_consumidos - gb_plan
        recarga = gb_extras * precio_gb_extra
        print(recarga)

elif tipo_cliente == "Prepago":
    print("Sin saldo")