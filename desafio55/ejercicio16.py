tipo_de_cliente = input("Tipo de cliente: ").lower()
plan_en_gb = 15
gasto_del_cliente_gb = 18
cobro_adicional = 0
if tipo_de_cliente == "postpago":
    if gasto_del_cliente_gb > plan_en_gb:
        cobro_adicional = gasto_del_cliente_gb - plan_en_gb
        cobro_adicional = cobro_adicional * 1000
        print(f"Usted debe {cobro_adicional}")
elif tipo_de_cliente == "prepago":
    print("Sin saldo")


    