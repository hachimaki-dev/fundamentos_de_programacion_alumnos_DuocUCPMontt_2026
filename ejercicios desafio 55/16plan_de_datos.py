tipo_de_cliente = "postpago"
plan_clienteGB = 15
GB_gastado = 18
GB_por_pagar = 0
if tipo_de_cliente == "postpago":
    if plan_clienteGB >= 15:
        GB_por_pagar = GB_gastado - plan_clienteGB
        plan_clienteGB = GB_por_pagar*1000
        print(f"{plan_clienteGB}")
else:
    tipo_de_cliente == "prepago" and plan_clienteGB > 15
    print("sin saldo")