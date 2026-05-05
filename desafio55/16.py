
cliente_tipo = "postpago"
plan_cliente = 15
gasto_del_plan_cliente = 18
cobro = 0
gigas_extra_usadas = 3
if cliente_tipo == "postpago":
    if gigas_extra_usadas > 0:
        cobro += 1000 * gigas_extra_usadas
        print(cobro)
elif cliente_tipo == "prepago":
    cobro += 0
    print("--Sin saldo--")


