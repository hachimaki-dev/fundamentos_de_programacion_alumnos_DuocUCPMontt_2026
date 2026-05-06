tipo_cliente = "postpago"
gigas_plan = 15
recargo = 0
gigas_gastados = 18

if tipo_cliente == "postpago":
    if gigas_gastados > gigas_plan:
        gigas_extra = gigas_gastados - gigas_plan
        recargo = gigas_extra * 1000
        print(recargo)
    else:
        print(0)
elif tipo_cliente == "prepago":
    print("sin saldo")
    