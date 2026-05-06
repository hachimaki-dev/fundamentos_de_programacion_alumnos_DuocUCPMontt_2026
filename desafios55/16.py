tipo_cliente = "Postpago"
gigas_plan = 15
gigas_gastados = 18

precio_giga_extra = 1000

if tipo_cliente == "Postpago":
    if gigas_gastados > gigas_plan:
        gigas_extra = gigas_gastados - gigas_plan
        recargo = gigas_extra * precio_giga_extra
        print(recargo)
    else:
        recargo = 0
        print(recargo)
else:
    print("Sin saldo")