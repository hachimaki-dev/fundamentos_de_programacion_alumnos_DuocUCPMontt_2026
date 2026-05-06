tipo_cliente = "Postpago"
plan = 15
gasto = 18

if tipo_cliente == "Postpago":
    cobro_extra_gb = 1000 * 3
    print(cobro_extra_gb)
    if tipo_cliente == "Prepago":
        cobro_extra_gb = 0
        print("Sin saldo")
