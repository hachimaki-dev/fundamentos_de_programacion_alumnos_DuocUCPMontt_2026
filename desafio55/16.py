plan_cliente_gygas = 15
cliente = "postpago"
uso_cliente_gygas = 18
cobro_x_giga_extra = 1000
extra = uso_cliente_gygas - plan_cliente_gygas
if cliente == "postpago":
    if uso_cliente_gygas > plan_cliente_gygas:
        cobro_final = extra*cobro_x_giga_extra
        print(cobro_final)
elif cliente == "prepago":
    print("sin saldo")